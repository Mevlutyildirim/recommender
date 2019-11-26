import React from "react";
import Card from "./card/card";
import axios from 'axios';

class Home extends React.Component {
  constructor(){
    super()
    this.state={
      datas:[{img:"deli.jpg", duration:"12", title:"merhaba"}]
    }
    
  }
  componentDidMount(){
    axios.get("http://127.0.0.1:5000/")
    .then(response => {
      console.log(response.data[0]);
      this.setState({datas:response.data})
    })
    .catch(error => {
      console.log(error);
    });
  }
  render() {
    return (
      <div>
        {this.state.datas.map((item,idx)=>{
          return <Card key={idx}  {...item}></Card>
        })}
      </div>
    );
  }
}

export default Home;
