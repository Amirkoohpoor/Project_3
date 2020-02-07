from flask import Flask, jsonify, render_template, request, redirect, url_for
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///toronto-real-estate.db' 

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Real_estate(db.Model):
   Mls_Number = db.Column(db.String(9), primary_key=True)
   Lat = db.Column(db.Float, nullable=False)
   Long = db.Column(db.Float, nullable=False)
   Street = db.Column(db.String(100), nullable=False)
   City = db.Column(db.String(10),nullable=False)
   Province = db.Column(db.String(10),nullable=False)
   Postal_Code = db.Column(db.String(10),nullable=False)
   Age = db.Column(db.String(10))
   Listed_By = db.Column(db.String(50))
   Lot_Size = db.Column(db.String(50))
   Size = db.Column(db.String(50))
   Style = db.Column(db.String(50))
   Taxes = db.Column(db.String(50))
   Type = db.Column(db.String(25))
   Walk_Score = db.Column(db.Integer)
   Neighbourhood = db.Column(db.String(20))
   Price = db.Column(db.Integer)
   Photo_url = db.Column(db.String(250))
   Date_posted_MLS = db.Column(db.String(15))

class Schema(ma.ModelSchema):
    class Meta:
        model = Real_estate


#landing page that will display all the postings in our database
#This function operate on the Read operation.
@app.route("/")
def home(): 
   return render_template("index.html")

@app.route("/api/real-estate-search-results")
def results(): 
   minprice = request.args.get('minprice')
   maxprice = request.args.get('maxprice')
   postings = Real_estate.query.filter_by(Price=maxprice).all()
   schema = Schema(many=True)
   output = schema.dump(postings).data
   return jsonify({"posting":output})

if __name__ == "__main__":
    app.run(debug=True)