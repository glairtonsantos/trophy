import React from 'react';

import axios from 'axios';


export default class MonsterList extends React.Component {
  state = {
    monsters: []
  }

  componentDidMount() {
    
    axios({
      method: 'get',
      url:`http://localhost:8000/monsters/`
    })
      .then(res => {
        const monsters = res.data.results;
        this.setState({ monsters });
      })
  }

  render() {
    return (
      <ul>
        { this.state.monsters.map(monster => <li><button>{monster.name}</button></li>)}
      </ul>
    )
  }
}