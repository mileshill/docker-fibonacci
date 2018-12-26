import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fib/<int:nsteps>')
def fib(nsteps):
    fib_number = compute_fibonacci(nsteps)
    return jsonify({'result': 'Ok', 'nsteps': nsteps, 'fib': fib_number})

def compute_fibonacci(n):
    if n <= 1:
        return n
    return compute_fibonacci(n-2) + compute_fibonacci(n-1)

if __name__ == '__main__':
    env_port = os.getenv('FLASK_PORT')
    env_debug = os.getenv('FLASK_DEBUG')
    app.run(host='0.0.0.0', port=env_port, debug=env_debug)