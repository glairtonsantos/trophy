import React from 'react';
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
        }
      }).catch(e => {
        console.log(e.response.data)
        alert('error in kill monster!')
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
            <input  type='hidden' name='monster' 
                    value={this.props.monster_item.id} 
                    ref={(input) => { this.monsterInput = input }} />
          <button type='submit'>{this.props.monster_item.name}</button>
        </form>
      </div>
    )
  }
}