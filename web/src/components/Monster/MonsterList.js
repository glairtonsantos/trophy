import React from 'react';
import API from '../../api';
import MonsterItem from './MonsterItem';
export default class MonsterList extends React.Component {
  state = {
    monsters: []
  }

  componentDidMount() {
    
    API.get(`monsters/`).then(res => {
      const monsters = res.data.results;
      this.setState({ monsters });
    })
      
  }

  render() {
    return (
      // <ul>
      //   { this.state.monsters.map(monster => <li><button>{monster.name}</button></li>)}
      // </ul>
      <ul>
        { this.state.monsters.map(monster => <li><MonsterItem monster_item={monster}></MonsterItem></li> )}
      </ul>
    )
  }
}