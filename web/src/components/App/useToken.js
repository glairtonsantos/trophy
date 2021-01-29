import { useState } from 'react';

export default function useToken() {

  const getToken = () => {
    const tokenString = localStorage.getItem('token');
    const userToken = JSON.parse(tokenString);
    return userToken?.token
  };

  const [token, setToken] = useState(getToken());

  const saveToken = userToken => {
    if(userToken.token){
      localStorage.setItem('token', JSON.stringify(userToken));
      setToken(userToken.token);
    }else{
      alert(JSON.stringify(userToken['non_field_errors'][0]));
    }
    
  };

  return {
    setToken: saveToken,
    token
  }

}