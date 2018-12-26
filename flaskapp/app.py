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
