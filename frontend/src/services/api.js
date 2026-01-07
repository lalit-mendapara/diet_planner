import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1',
});

export const generateDietPlan = async (surveyData) => {
  try {
    const response = await API.post('/generate-plan', surveyData);
    return response.data;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};