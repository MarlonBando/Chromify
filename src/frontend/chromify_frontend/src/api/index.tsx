import axios from 'axios';

const API_URL = 'http://0.0.0.0:8000/infer';

export const callApi = async (data: any) => {
    try {
        const response = await axios.post(API_URL, data);
        return response.data;
    } catch (error) {
        console.error('Error calling API:', error);
        throw error;
    }
};
