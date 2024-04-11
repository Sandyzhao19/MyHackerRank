import React, { Component } from 'react';
import './App.css';

import EmployeeInfo from './components/EmployeeInfo';

class App extends Component {
  render() {
    const { employees } = this.props;
    return (
      <div className="App">
        <EmployeeInfo employees={employees} />
      </div>
    );
  }
}

export default App;