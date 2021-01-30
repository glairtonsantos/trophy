import React from 'react';
import ListGroup from 'react-bootstrap/ListGroup';

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
      <div className="col-4">
        <ListGroup>
          { this.state.monsters.map(monster => 
            <ListGroup.Item>
              <MonsterItem monster_item={monster}></MonsterItem>
            </ListGroup.Item> 
          )}
        </ListGroup>
      </div>
    )
  }
}