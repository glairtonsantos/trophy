import React from 'react';
import API from '../../api';

export default class CollectCoin extends React.Component {
  state = {
    value_coin: 10
  }

  handleChange = event => {
    this.setState({ value_coin: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    const user_request = {
      value: this.state.value_coin
    };

    API.post(`coins/collect/`, user_request)
      .then(res => {
        if(res.status === 201){
          console.log(res);
          console.log(res.data);
          document.getElementById('form-id-coin').reset();
        }
      }).catch(e => {
        console.log(e.response.data)
        alert('error in collect coin!')
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit} id='form-id-coin'>
          <label>
            value coin:
            <input type='number' name='value_coin' onChange={this.handleChange} />
          </label>
          <button type='submit'>Collect Coin!</button>
        </form>
      </div>
    )
  }
}