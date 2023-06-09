import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true,
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  async getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  async getQuestion(position) 
  {
    return this.call("get", "questions?position="+position)
  },
  async getQuestionByid(position) 
  {
    return this.call("get", "questions/"+position)
  },
  async getAllQuestions(token) {
    return this.call("get", "questions/all",null,token);
  },
  async getScores() {
    return this.call("get", "scores");
  },
  async addQuestion(data,token){
    return this.call("post", "questions",data,token);
  },
  async updtquestion(id,token,data){
    return this.call("put","questions/"+id,data,token)
  },
  async deleteAllQuestions(token) {
    return this.call("delete", "questions/all",null,token);
  },
  async DeleteParticipations(token) {
    return this.call("delete", "participations/all",null,token);
  },
  async deleteQuestion(id,token) {
    return this.call("delete", "questions/"+id,null,token);
  },
  async submitParticipation(playerName, answers) {
    const answersArray = Object.values(answers);
    const data = {
      "playerName": playerName,
      "answers": answersArray
  };
    console.log('Data to be sent:', data);
    try {
      const response =this.call("post", "participations",data);
      console.log(response)
      return response;
    } catch (error) {
      console.error('Error submitting participation:', error);
      throw error;
    }
  },
  async adminLogin(pPassword) {
    const data = {
      "password": pPassword,
    };

    try {
      const response = await this.call("post", "login", data);
      return response;
    } catch (error) {
      console.error("Error logging in:", error);
      throw error;
    }
  },
  
};
