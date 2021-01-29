import React from 'react';
import axios from 'axios';

export default class CollectCoin extends React.Component {
  state = {
    user_id: '',
    value_coin: 10
  }

  handleChangeUser = event => {
    this.setState({ user_id: event.target.value });

  }
  handleChangeCoin = event => {
    this.setState({ value_coin: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    const user_request = {
      user: this.state.user_id,
      value: this.state.value_coin
    };

    axios.post(`http://localhost:8000/coins/collect/`, user_request)
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            user id and value coin:
            <input type="number" name="user_id" onChange={this.handleChangeUser} />
            <input type="number" name="value_coin" onChange={this.handleChangeCoin} />
          </label>
          <button type="submit">Collect Coin!</button>
        </form>
      </div>
    )
  }
}