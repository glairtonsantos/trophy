import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import Panel from '../Panel/Panel';
import Login from '../Login/Login';
import useToken from './useToken';
import MonsterList from '../Monster/MonsterList';
import CollectCoin from '../Coin/CollectCoin';
import Death from '../Death/Death';
import TrophyList from '../Trophy/TrophyList';

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
      <div className="row">
        <CollectCoin></CollectCoin>
        
        <MonsterList></MonsterList>
        
        <Death></Death>
      </div>

      <hr></hr>
      <h3>User - Trophies</h3>
      <TrophyList></TrophyList>

    </div>
  );
}

export default App;