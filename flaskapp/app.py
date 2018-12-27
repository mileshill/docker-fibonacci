import os
import redis
import time
from flask import Flask, jsonify

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def compute_fibonacci(n):
    if n <= 1:
        return n
    return compute_fibonacci(n-2) + compute_fibonacci(n-1)

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
    env_port = os.getenv('FLASK_PORT')
    env_debug = os.getenv('FLASK_DEBUG')
    app.run(host='0.0.0.0', port=env_port, debug=env_debug)