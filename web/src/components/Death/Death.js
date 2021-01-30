import React from 'react';
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
        }
      }).catch(e => {
        console.log(e.response.data)
        alert('error in user die!')
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit} id='form-id-death'>
          <button type='submit'>User Die!</button>
        </form>
      </div>
    )
  }
}