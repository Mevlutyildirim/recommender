import React from "react";
import "./card.css";
import Button from '@material-ui/core/Button';
import axios from 'axios';

export default class Card extends React.Component{
  constructor(){
    super();
  }

  send(movie_id, is_liked){
    console.log({movie_id, is_liked});
    axios.post("http://127.0.0.1:5000/actions", {movie_id, is_liked}).then(res=>{
      console.log(res.data);
    }).catch(e =>{
      console.log(e);
    })
  }

  render(){
    const {id, duration, type, cover, title, year, rate, votes, link, details, director} = this.props;
    return (
      <div className="card">
        <div className="card__poster">
          <img src={cover} alt="" width="140" height="209" />
        </div>
        <div className="card__content">
          <div>
            <h2 className="card__title"><a href={link}>{title}</a><small>{year}</small></h2>
          </div>
          <div className="card__cast">
            <span>{duration} min |</span>
            <span>{type} </span>
          </div>
          <div>
            <span>rate: {rate} </span>
          </div>
          <p className="card__details">
            {details}
          </p>
          <div className="card__cast">
            <span>Director: {director}</span>
          </div>
          <div className="card__cast">
            <span>Votes: {votes}</span>
          </div>
          <div>
            <Button size="small" color="primary" onClick={this.send.bind(this, id, "like")}>like</Button>
            <Button onClick={this.send.bind(this, id, "dislike")}>dislike</Button>
          </div>
        </div>
      </div>
    );
  }
}
