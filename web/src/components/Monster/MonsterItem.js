import React from 'react';
import { Form, Button } from 'react-bootstrap';

import API from '../../api';

export default class MonsterItem extends React.Component {

  
  handleSubmit = event => {
    event.preventDefault();

    const monster_request = {
        monster: this.monsterInput.value,
    };

    API.post(`monsters/kill/`, monster_request)
      .then(res => {
        if(res.status === 201){
          console.log(res);
          console.log(res.data);
          alert('Killed Monster!');
        }
      }).catch(e => {
        console.log(e.response.data)
        alert('error in kill monster!')
      })
  }

  render() {
    return (
      <div>
        <Form onSubmit={this.handleSubmit}>
            <input  type='hidden' name='monster' 
                    value={this.props.monster_item.id} 
                    ref={(input) => { this.monsterInput = input }} />
          <Button variant="outline-danger" type='submit'>kill {this.props.monster_item.name}!</Button>
        </Form>
      </div>
    )
  }
}