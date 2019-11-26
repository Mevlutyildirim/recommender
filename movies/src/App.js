import React from "react";
import './app.css';
import Header from './components/header';
import {Switch, Route} from 'react-router-dom';
import Home from './home';
import Login from './login';

class App extends React.Component {
  
  render(){
    return(
      <React.Fragment>
        <Header/>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route path="/login" component={Login}/>
      </Switch>
      </React.Fragment>
    )
  }
    
}

export default App;
