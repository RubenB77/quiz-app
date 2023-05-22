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
  async getQuestion(position) {
    return this.call("get", `questions/${position}`)
  },
  async getScores() {
    return this.call("get", "scores");
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
      //const response = await axios.post('/participations', data);
      return response.data;
    } catch (error) {
      console.error('Error submitting participation:', error);
      throw error;
    }
  },
  
};
