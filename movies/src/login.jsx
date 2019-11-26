import React from 'react'
import axios from 'axios';
import Card from './card/card';

export default class Login extends React.Component{
  constructor(){
    super()
    this.state={
      datas:[{img:"deli.jpg", duration:"12", title:"merhaba"}]
    }
    
  }
  componentDidMount(){
    axios.get("http://127.0.0.1:5000/")
    .then(response => {
      this.setState({datas:response.data})
    })
    .catch(error => {
      console.log(error);
    });
  }
  render() {
    return (
      <React.Fragment>
        <div className="status-bar">
          <div>liked:<span className="liked">13</span></div>
          <div>disliked: <span className="disliked">12</span></div>
        </div>
      <div>
        {this.state.datas.map((item,idx)=>{
          return <Card key={item.id}  {...item}></Card>
        })}
      </div>
      </React.Fragment>
    );
  }
}