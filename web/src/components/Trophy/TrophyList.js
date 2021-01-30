import React from 'react';
import API from '../../api';
import Table from 'react-bootstrap/Table';

export default class TrophyList extends React.Component {
  state = {
    trophies: []
  }

  componentDidMount() {
    
    API.get(`trophies`).then(res => {
      const trophies = res.data;
      this.setState({ trophies });
    })
      
  }

  render() {
    return (
      <div>
        
        <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>Trophies</th>
              <th>Amount</th>
              <th>Detail</th>
            </tr>
          </thead>
          <tbody>
            { this.state.trophies.map(item => 
              <tr>
                <td>{item.trophy.category.description}</td>
                <td>{item.trophy.level.amount}</td>
                <td>{item.value_register_field}</td>
              </tr>)
            }
          </tbody>
        </Table>

      </div>
    )
  }
}