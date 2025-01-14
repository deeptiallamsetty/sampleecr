from flask import Flask, jsonify
import awsgi

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

def handler(event, context):
    return awsgi.response(app, event, context)
