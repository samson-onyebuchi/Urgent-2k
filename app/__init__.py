import os
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
from pymongo import MongoClient
from config import Config, MONGO_URI


# from flask_pymongo import PyMongo

# Initialize application
app = Flask(__name__)

# app configuration
app.config.from_object(Config)

# Initialize Flask Api
api = Api(app)

CORS(app)
#Initialize db
client = MongoClient(os.getenv("MONGO_URI"))
db = client.urgent2k
wallets = db.wallets

# Import the application webservice
from app import webservice, error