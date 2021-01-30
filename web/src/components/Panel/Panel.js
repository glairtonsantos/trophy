import React from 'react';
import { Table } from 'react-bootstrap';
import API from '../../api';

export default class Panel extends React.Component {
  state = {
    details: []
  }

  componentDidMount() {
    API.get(`user/detail/`).then(res => {
      let details = res.data;
      this.setState({ details });
      console.log(this.state);
    });
  }

  render() {
    return(
      <div className="col-6">
        <Table striped bordered >
          <thead>
            <tr>
              <th># coins</th>
              <th># dead monsters</th>
              <th># deaths</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{this.state.details.coins}</td>
              <td>{this.state.details.killed_monsters}</td>
              <td>{this.state.details.deaths}</td>
            </tr>
          </tbody>
        </Table>
      </div>
    )
  }
}