import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';
import Panel from '../Panel/Panel';
import Login from '../Login/Login';
import useToken from './useToken';
import MonsterList from '../Monster/MonsterList';
import CollectCoin from '../Coin/CollectCoin';
import Death from '../Death/Death';

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
          <Route path="/painel">
            <Panel />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
        </Switch>
      </BrowserRouter>
      <hr></hr>
      <MonsterList></MonsterList>
      <hr></hr>
      <CollectCoin></CollectCoin>
      <hr></hr>
      <Death></Death>

    </div>
  );
}

export default App;