import React from 'react';
import API from '../../api';

export default class TrophyList extends React.Component {
  state = {
    trophies: []
  }

  componentDidMount() {
    
    API.get(`trophies`).then(res => {
      const trophies = res.data;
      this.setState({ trophies });
    })
      
  }

  render() {
    return (
      <ul>
        { this.state.trophies.map(item => <li>{item.trophy.category.description}: {item.trophy.level.amount}</li>)}
      </ul>
    )
  }
}