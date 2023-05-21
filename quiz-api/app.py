from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import jwt_utils
import sql
from question import (
    CreateQuestion,
    DeleteQuestions,
    GetQuestionbyID,
    GetQuestionbyPosJSON,
    DeleteQuestionById,
    UpdQuestionByID,
    GetSizeQuestions,
    CreateParticipation,
    DeleteParticipations,
    GetScores,
)

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Hello, world"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return jsonify({"size": GetSizeQuestions(), "scores": GetScores()}), 200

@app.route('/login', methods=['POST'])
def Login():
    payload = request.get_json()
    tried_password = payload['password'].encode('UTF-8')
    hashed = hashlib.md5(tried_password).digest()
    if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
        token = jwt_utils.build_token()
        return jsonify({"token": token}), 200
    else:
        return 'Unauthorized', 401

def checkAuth():
    token = request.headers.get('Authorization')
    if token:
        try:
            jwt_utils.decode_token(token.replace("Bearer ", ""))
            return True
        except jwt_utils.JwtError:
            return False
    else:
        return False

@app.route('/questions', methods=['POST'])
def AddQuestion():
    if checkAuth():
        input = request.get_json()
        response = CreateQuestion(input)
        return jsonify(response), 200
    else:
        return 'Unauthorized', 401

@app.route('/questions', methods=['GET'])
def PosQestion():
    position = request.args.get('position')
    response = GetQuestionbyPosJSON(position)
    if response == None:
        return 'No question with this pos', 404
    return jsonify(response), 200

@app.route('/questions/all', methods=['DELETE'])
def DelAllQuestions():
    if checkAuth():
        DeleteQuestions()
        return 'All Questions Deleted', 204
    else:
        return 'Unauthorized', 401

@app.route('/questions/<questionId>', methods=['GET'])
def GetQuestionById(questionId):
    response = GetQuestionbyID(questionId)
    if response == None:
        return 'No question with this id', 404
    return jsonify(response), 200

@app.route('/questions/<questionId>', methods=['DELETE'])
def DelQuestionById(questionId):
    if checkAuth():
        response = DeleteQuestionById(questionId)
        if response == None:
            return 'No question with this id', 404
        return "Question " + questionId + " is deleted", 204
    else:
        return 'Unauthorized', 401

@app.route('/questions/<questionId>', methods=['PUT'])
def UpdQuestionById(questionId):
    input = request.get_json()
    response = UpdQuestionByID(input, questionId)
    if response == None:
        return 'No question with this id', 404
    return jsonify(response), 204

@app.route('/participations', methods=['POST'])
def AddParticipation():
    input = request.get_json()
    response = CreateParticipation(input)
    if response == None:
        return 'Bad request', 400
    return jsonify(response), 200

@app.route('/participations/all', methods=['DELETE'])
def DelAllParticipation():
    if checkAuth():
        DeleteParticipations()
        return 'All participations Deleted', 204
    else:
        return 'Unauthorized', 401

if __name__ == "__main__":
    app.run()
