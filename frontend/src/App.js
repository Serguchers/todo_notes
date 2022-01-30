import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js';
import MenuItem from './components/Menu';
import FooterItem from './components/Footer';
import {ProjectList, ProjectDetail} from './components/Projects'
import ToDoList from './components/ToDos'
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import LoginForm from './components/Auth';
import axios from 'axios';
import Cookies from 'universal-cookie'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todos': [],
      'token': ''
    }
  }

  get_token(username, password) {
    // Отправляем post-запрос на адрес, где наш API сгенерирует токен для пользователя
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
      this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }

  set_token(token) {
    // Метод set_token принимает токен, устанавливает его в cookies и записывает состояние приложения.
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token}, ()=>this.load_data())
  }

  is_authenticated() {
    // Метод будет определять авторизован пользователь или нет. Он авторизован, если токен в состоянии не пустой.
    return this.state.token != ''
  }

  logout() {
    // Метод logout() обнуляет токен
    this.set_token('')
  }

  get_token_from_storage() {
    // Данный метод нужен при повторном открытии страницы сайта. Он считывает токен из cookies и записывает его в состояние.
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token}, ()=>this.load_data())
  }

  get_headers() {
    // Если пользователь авторизован, то в заголовки запроса мы добавляем ключ Authorization со значением токена.
    let headers = {
      'Content-type': 'application/json'
    }
    if (this.is_authenticated()) {
      headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }

  load_data() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/users', {headers})
    .then(response => {
      const users = response.data.results
      this.setState(
        {
          'users': users
        }
      )
    }).catch(error => console.log(error)) 

    axios.get('http://127.0.0.1:8000/api/projects', {headers})
    .then(response => {
      const projects = response.data.results
      this.setState(
        {
          'projects': projects
        }
      )
    }).catch(error => console.log(error)) 

    axios.get('http://127.0.0.1:8000/api/todos', {headers})
    .then(response => {
      const todos = response.data.results
      this.setState(
        {
          'todos': todos
        }
      )
    }).catch(error => console.log(error)) 
  }

  componentDidMount() {
    this.get_token_from_storage()
  }

  render () {
    return (
      <div>
        <MenuItem/>
        <BrowserRouter>
          <Switch>
            <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
            <Route exact path='/' component={() =><UserList users={this.state.users}/> }/>
            <Route exact path='/projects' component={() =><ProjectList projects={this.state.projects}/>}/>
            <Route exact path='/todos' component={() =><ToDoList todos={this.state.todos}/>}/>
            <Route exact path="/projects/:id">
              <ProjectDetail projects={this.state.projects}/>
            </Route>
          </Switch>
        </BrowserRouter>
        <FooterItem/>
      </div>
    )
  }
}

export default App;
