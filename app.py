
from flask import Flask, jsonify, request
from ml_news_core import similarNews

app = Flask(__name__)

@app.route("/")
def index():
    return "Machine Learning API for Balanced News Summary" # Just updating my code

@app.route("/ml-related-news",methods=["GET"])
def api():
    args = request.args
    if "url" in args:
        try:
            print(args["url"])
            print("working")
            result_dict = similarNews(args["url"])
            return jsonify(result_dict)
        except Exception as e:
            return jsonify({"Error":str(e)})