import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js';
import MenuItem from './components/Menu';
import FooterItem from './components/Footer';
import ProjectList from './components/Projects'
import ToDoList from './components/ToDos'
import {BrowserRouter, Route} from 'react-router-dom'
import axios from 'axios';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todos': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users')
    .then(response => {
      const users = response.data.results
      this.setState(
        {
          'users': users
        }
      )
    }).catch(error => console.log(error)) 

    axios.get('http://127.0.0.1:8000/api/projects')
    .then(response => {
      const projects = response.data.results
      this.setState(
        {
          'projects': projects
        }
      )
    }).catch(error => console.log(error)) 

    axios.get('http://127.0.0.1:8000/api/todos')
    .then(response => {
      const todos = response.data.results
      this.setState(
        {
          'todos': todos
        }
      )
    }).catch(error => console.log(error)) 
  }

  render () {
    return (
      <div>
        <MenuItem/>
        <BrowserRouter>
          <Route exact path='/' component={() =><UserList users={this.state.users}/> }/>
          <Route exact path='/projects' component={() =><ProjectList projects={this.state.projects}/>}/>
          <Route exact path='/todos' component={() =><ToDoList todos={this.state.todos}/>}/>
        </BrowserRouter>
        <FooterItem/>
      </div>
    )
  }
}

export default App;
