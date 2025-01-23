import axios from 'axios';
import { ApiResponseColorizedImage } from './interface';
const API_URL = 'http://0.0.0.0:8000/infer';

export const callApi = async (data: any) => {
    try {
        const response = await axios.post<ApiResponseColorizedImage>(API_URL, data);
        console.log('API response:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error calling API:', error);
        throw error;
    }
};
