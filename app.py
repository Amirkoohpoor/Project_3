from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, Real_estate

#Connect to Database and create database session
engine = create_engine('sqlite:///toronto-real-estate.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#landing page that will display all the postings in our database
#This function operate on the Read operation.

@app.route("/")
def showPostings():
   postings = session.query(Real_estate).all()
   return render_template("index.html", postings=postings)


if __name__ == "__main__":
    app.run(debug=True)