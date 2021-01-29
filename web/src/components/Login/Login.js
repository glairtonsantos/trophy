import React, { useState } from 'react';
import PropTypes from 'prop-types';
import API from '../../api';

import './Login.css';

async function loginUser(credentials) {
  let request = JSON.stringify(credentials)
  return API.post(`api-token-auth/`,
    request,
    {headers: {
      'Content-Type': 'application/json'
    }}).then(
      res => {
        if(res.status == 200){
          let token = res.data.token
          return token
        }
      }
    )
}
export default function Login({ setToken }) {
  const [username, setUserName] = useState();
  const [password, setPassword] = useState();

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      username,
      password
    });
    setToken(token);
  }

  return(
    <div className="login-wrapper">
      <h1>Please Log In</h1>
    <form onSubmit={handleSubmit}>
      <label>
        <p>Username</p>
        <input type="text"  onChange={e => setUserName(e.target.value)}/>
      </label>
      <label>
        <p>Password</p>
        <input type="password" onChange={e => setPassword(e.target.value)} />
      </label>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
    </div>
  )
}

Login.propTypes = {
  setToken: PropTypes.func.isRequired
}