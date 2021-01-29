import React, { useState } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';
import Panel from '../Panel/Panel';
import Login from '../Login/Login';
import useToken from './useToken';

function App() {
  const { token, setToken } = useToken();

  if(!token) {
    return <Login setToken={setToken} />
  }

  return(
    <div className="wrapper">
      <h1>Trophy - Ribon</h1>
      <BrowserRouter>
        <Switch>
          <Route path="/home">
            <Panel />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;