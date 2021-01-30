import React from 'react';
import { Form, Button } from 'react-bootstrap';

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
      <div className="col-4">
        <Form inline  onSubmit={this.handleSubmit} id='form-id-coin'>
            <Form.Control 
              type='number' 
              name='value_coin' 
              placeholder='value coin'
              onChange={this.handleChange}>

            </Form.Control>
          <Button  variant="outline-warning" type='submit'>Collect Coin!</Button>
        </Form>
      </div>
    )
  }
}