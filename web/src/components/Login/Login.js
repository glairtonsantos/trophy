import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Button, Form, Row, Col, Container } from 'react-bootstrap';

import API from '../../api';
import './Login.css';

async function loginUser(credentials) {
  let request = JSON.stringify(credentials)
  return API.post(`api-token-auth/`,
    request,
    {headers: {
      'Content-Type': 'application/json'
    }}).then(
      res => {
        if(res.status == 200){
          let token = res.data.token
          return token
        }
      }
    ).catch(e => {
      console.log(e.response.data)
      alert('Ops! verify your username or password')
    })
}
export default function Login({ setToken }) {
  const [username, setUserName] = useState();
  const [password, setPassword] = useState();

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      username,
      password
    });
    setToken(token);
    window.location.reload();
  }

  return(
    <Container>
      <div className="login-wrapper">
        <h1>Please Log In</h1>
        <Form onSubmit={handleSubmit} className="login-div">
          <Form.Group as={Row} controlId="formHorizontalEmail">
              <Form.Label>
              Username
              </Form.Label>
              <Col>
                <Form.Control type="text" placeholder="Username"  onChange={e => setUserName(e.target.value)} />
              </Col>
          </Form.Group>
          
          <Form.Group as={Row} controlId="formHorizontalPassword">
              <Form.Label>
                Password
              </Form.Label>
              <Col>
                <Form.Control type="password" placeholder="Password"  onChange={e => setPassword(e.target.value)} />
              </Col>
          </Form.Group>
          <Form.Group className="login-btn">
            <Button variant="primary" type="submit">
              Login
            </Button>
          </Form.Group>
        </Form>
      </div>
    </Container>
  )
}

Login.propTypes = {
  setToken: PropTypes.func.isRequired
}