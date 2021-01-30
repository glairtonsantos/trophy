import React from 'react';
import { Form, Button } from 'react-bootstrap';

import API from '../../api';

export default class Death extends React.Component {

  handleSubmit = event => {
    event.preventDefault();

    API.post(`users/die/`)
      .then(res => {
        if(res.status === 201){
          console.log(res);
          console.log(res.data);
          document.getElementById('form-id-death').reset();
          alert('User Die!');
          window.location.reload();
        }
      }).catch(e => {
        console.log(e.response.data)
        alert('error in user die!')
      })
  }

  render() {
    return (
      <div className="col-4">
        <Form onSubmit={this.handleSubmit} id='form-id-death'>
          <Button variant="outline-dark" type='submit'>User Die!</Button>
        </Form>
      </div>
    )
  }
}