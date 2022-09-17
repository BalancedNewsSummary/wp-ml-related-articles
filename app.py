
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/")
def index():
    return "Machine Learning API for Balanced News Summary" # Just updating my code