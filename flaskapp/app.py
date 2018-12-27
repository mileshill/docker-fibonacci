import os
from functools import reduce
import redis
import time
from flask import Flask, jsonify

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def compute_fibonacci(n):
    a = 1
    b = 1
    c = a + b
    count = 4
    while count <= n:
        a = b
        b = c
        c = a + b
        count += 1
    return c

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.05)

@app.route('/fib/<int:nsteps>')
def fib(nsteps):
    hits = get_hit_count()
    fib_number = compute_fibonacci(nsteps)
    return jsonify({'result': 'Ok', 'nsteps': nsteps, 'fib': fib_number, 'hits': hits})

if __name__ == '__main__':
    env_port = os.getenv('FLASK_PORT', 5000)
    env_debug = os.getenv('FLASK_DEBUG', True)
    app.run(host='0.0.0.0', port=env_port, debug=env_debug)