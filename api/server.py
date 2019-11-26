from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1729Light",
    database="ml",
     use_pure=True
)

mycursor = mydb.cursor()

recommend = pd.read_sql("select * from movies where state is null", con=mydb)
dataframe = pd.DataFrame(recommend)
sended = dataframe.to_json(orient="records")
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
  return sended

@app.route('/actions', methods=["POST"])
def action():
  content = request.json
  is_liked = content["is_liked"]
  movie_id = content["movie_id"]
  sql ="update movies set state= %s where id=%s"
  val = (is_liked, movie_id)
  mycursor.execute(sql, val)
  mydb.commit()
  return {"deneme": is_liked}

@app.route('/login', methods=["POST"])
def login():
  return sended



if __name__ == '__main__':
  app.run()