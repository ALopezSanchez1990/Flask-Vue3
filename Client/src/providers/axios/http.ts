import axios, { type AxiosInstance } from 'axios'

const apiClient: AxiosInstance = axios.create({
  baseURL: 'https://api.openbrewerydb.org',
  headers: {
    'Content-type': 'application/json',
  },
})

export default apiClient