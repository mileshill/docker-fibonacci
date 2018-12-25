from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/debug')
def debug():
    return jsonify({'result': 'App is working'})