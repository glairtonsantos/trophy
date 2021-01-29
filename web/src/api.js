import axios from 'axios';

const loadToken = () => {
    const tokenString = localStorage.getItem('token');
    const userToken = JSON.parse(tokenString);
    return userToken
};
const authtoken = loadToken();

const baseConfig = {
    baseURL: `http://localhost:8000/`
}

if(authtoken){
  baseConfig['headers'] = {
    Authorization: `Token ${authtoken}`
  }
}

export default axios.create(baseConfig);