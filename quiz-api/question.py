import jwt_utils
import sql
import sqlite3
import json

class Question():
    def __init__(self, id: int, position: int, title: str, text: str, image: str, possibleAnswers=None):
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image
        self.possibleAnswers = []
        if(possibleAnswers):
            for answer in possibleAnswers:
                self.possibleAnswers.append({
                'text': answer['text'],
                'isCorrect': answer['isCorrect']})



def ConvertToQuestion(request: str):
    if(request["possibleAnswers"]):
        return Question(None,
        request["position"],
        request["title"],
        request["text"],
        request["image"],
        request["possibleAnswers"])
    else:
        return Question(None,
        request["position"],
        request["title"],
        request["text"],
        request["image"])
    
def DataToAnswerList(answer: tuple):
    answer_list = []
    
    for ans in answer:
        if ans[3]=='True':
            answer_list.append({
            'text': ans[2],
            'isCorrect': True})
        if ans[3]=='False':
            answer_list.append({
            'text': ans[2],
            'isCorrect': False})
        if ans[3]==0:
            answer_list.append({
            'text': ans[2],
            'isCorrect': False})
        if ans[3]==1:
            answer_list.append({
            'text': ans[2],
            'isCorrect': True})

        
    
    return answer_list

def DataToQuestion(data: tuple):
    return Question(
        data[0],
        data[1],
        data[2],
        data[3],
        data[4]
    )

def ConvertToJson(question: Question):
    if(hasattr(question,"possibleAnswers")):
        return {
        "id": question.id,
        "title": question.title,
        "text": question.text,
        "image": question.image,
        "position": question.position,
        "possibleAnswers": question.possibleAnswers
    }
    else :
        return {
        "id": question.id,
        "position": question.position,
        "title": question.title,
        "text": question.text,
        "image": question.image}

def FuseQuestionAnswer(question,answer):
    return Question(question.id,question.position,question.title,question.text,question.image,answer)

def GetQuestionbyPos(position):
    db = sql.CreateConnection()
    db.execute("SELECT * FROM questions WHERE position=?", (position,))
    question = db.fetchone()
    db.close()
    return question

def GetQuestionbyPosJSON(position):
    question =GetQuestionbyPos(position)
    if question==None:
        return None
    response = GetQuestionbyID(question[0])
    return response

def GetQuestionbyID(pId):
    db = sql.CreateConnection()
    db.execute("SELECT * FROM questions WHERE id=?", (pId,))
    data = db.fetchone()
    if data==None:
        return None
    db.execute("SELECT * FROM answers WHERE idQuestion=?", (pId,))
    question = DataToQuestion(data)
    answer=db.fetchall()
    if answer==None:
        db.close()
    else :
        answer = DataToAnswerList(answer)
        question = FuseQuestionAnswer(question,answer)
        db.close()
    questionJson = ConvertToJson(question)
    return questionJson


def UpdQuestionByID(input,pId):
    db = sql.CreateConnection()
    db.execute(f"SELECT position FROM questions WHERE id = {pId}")
    pos = db.fetchone()[0]

    db.execute("SELECT * FROM questions WHERE id=?", (pId,))
    data = db.fetchone()
    if data==None:
        return None
    input = ConvertToQuestion(input)
    db.execute("begin")
    insertion = db.execute("""UPDATE questions SET position = ? WHERE id = ?;""", (None, pId))

    db.execute("SELECT * FROM questions ORDER BY position ")
    questions = db.fetchall() 
    pos=0 
    for question in questions:
        if question[1]!=None:
            pos=pos+1
            db.execute(f"UPDATE questions SET position = {pos} WHERE position = {question[1]}")
    FreePosition(input.position,db)
    insertion = db.execute("""UPDATE questions SET position = ?,title = ?, text = ?,image = ? WHERE id = ?;""", (input.position, input.title, input.text, input.image, pId))
    
    if(input.possibleAnswers):
        db.execute(f"DELETE FROM answers WHERE idQuestion=?", (pId,))
        for answer in input.possibleAnswers:
            db.execute(
            f"INSERT INTO answers (idQuestion, text, isCorrect) VALUES"
            f"('{pId}', '{answer['text']}', '{answer['isCorrect']}')")
    db.execute("commit")
    db.close()
    response = ConvertToJson(input)
    return response


    
def FillPositionGap(position_to_fill, conn):

    question_to_fill = GetQuestionbyPos(position_to_fill)
    if question_to_fill is None:
        return

    conn.execute("SELECT MAX(position) FROM questions")
    max_position = conn.fetchone()[0]

    for position in range(position_to_fill + 1, max_position + 1):
        conn.execute(f"UPDATE questions SET position = {position - 1} WHERE position = {position}")

    conn.execute(f"UPDATE questions SET position = {max_position} WHERE position IS NULL")



def FreePosition(position_to_free,conn):
    question_to_free = GetQuestionbyPos(position_to_free) 
    if question_to_free is None:
        return
    conn.execute('SELECT position FROM questions ORDER BY position')
    positions = [row[0] for row in conn.fetchall()]
    pos=positions[-1]
    while pos>=position_to_free:
        new_pos = pos + 1
        conn.execute(f"UPDATE questions SET position = {new_pos} WHERE position = {pos}")
        pos=pos-1



def CreateQuestion(input):   
    question = ConvertToQuestion(input)
    
    database = sql.CreateConnection()

    FreePosition(question.position,database)
    database.execute("begin")
    
    insertion = database.execute("""INSERT INTO questions (position, title, text, image) VALUES (?, ?, ?, ?)""",(question.position, question.title, question.text, question.image))
    
    question.id = insertion.lastrowid  
    if question.possibleAnswers:
        for answer in question.possibleAnswers:
            database.execute("""INSERT INTO answers (idQuestion, text, isCorrect) VALUES (?, ?, ?)""",(question.id, answer['text'], answer['isCorrect']))
    database.execute("commit")
    database.close()
    response = ConvertToJson(question)
    return response


def DeleteQuestions():
    database = sql.CreateConnection()
    database.execute("begin")
    database.execute(f"DELETE FROM questions;")
    database.execute(f"DELETE FROM answers;")
    database.execute(f"UPDATE sqlite_sequence SET seq=0 WHERE name='questions';")
    database.execute(f"UPDATE sqlite_sequence SET seq=0 WHERE name='answers';")
    database.execute("commit")
    database.close()

def DeleteQuestionById(questionId):
    database = sql.CreateConnection()
    database.execute("begin")
    database.execute("SELECT * FROM questions WHERE id=?", (questionId,))
    data = database.fetchone()
    if data==None:
        database.close()
        return None
    database.execute(f"DELETE FROM questions WHERE id=?", (questionId,))
    database.execute(f"DELETE FROM answers WHERE idQuestion=?", (questionId,))
    database.execute("SELECT * FROM questions ORDER BY position ")
    questions = database.fetchall() 
    pos=0 
    for question in questions:
        pos=pos+1
        database.execute(f"UPDATE questions SET position = {pos} WHERE position = {question[1]}")
    database.execute("commit")
    database.close()
    return 1

def GetSizeQuestions():
    database = sql.CreateConnection()
    database.execute("SELECT COUNT(*) FROM questions")
    result = database.fetchone()
    count = result[0]
    database.close()
    return count


def CreateParticipation(input): 
    NbQuestion = GetSizeQuestions()
    NbReponse = len(input['answers'])
    if NbQuestion!=NbReponse:
        return None
    database = sql.CreateConnection()
    scoreplayer=calculate_score(input['answers'])
    database.execute("begin")
    database.execute(
        f"INSERT INTO participations (playerName, answers, score) VALUES"
        f"('{input['playerName']}', '{input['answers']}', '{scoreplayer}')")
    database.execute("commit")
    database.close()
    return {"playerName": input['playerName'],"answers": input['answers'],"score":scoreplayer}

def DeleteParticipations():
    database = sql.CreateConnection()
    database.execute("begin")
    database.execute(f"DELETE FROM participations;")
    database.execute(f"UPDATE sqlite_sequence SET seq=0 WHERE name='participations';")
    database.execute("commit")
    database.close()

def calculate_score(answers):
    database = sql.CreateConnection()
    database.execute("SELECT * FROM questions ORDER BY position ")
    questions = database.fetchall()
    pos=0
    score =0
    for question in questions:
        pos=pos+1
        database.execute("SELECT * FROM answers WHERE idQuestion=?", (question[0],))
        fetchanswers =database.fetchall()
        if fetchanswers[answers[pos-1]-1][3]==True:
            score = score+1
    database.close()
    return score

def GetScores():
    database = sql.CreateConnection()
    database.execute("SELECT * FROM participations ORDER BY score DESC")
    result = database.fetchall()
    response = []
    for participant in result :
        response.append({"playerName": participant[1],"score":participant[3]})
    database.close()
    return response

def GetAllQuestions():
    database = sql.CreateConnection()
    database.execute("SELECT * FROM questions ORDER BY position ")
    response = database.fetchall() 
    database.close()
    return response