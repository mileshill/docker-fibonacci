import pytest
from flaskapp.app import app, compute_fibonacci


@pytest.fixture(scope='module')
def client():
    yield app.test_client()

def test_fibonacci_response(client):
    response = client.get('fib/10')
    assert response.status == '200 OK'

def test_fibonacci_value_recursive(client):
    result = compute_fibonacci(5)
    assert result == 5

def test_compute_fibonacci_base_case(client):
    result = compute_fibonacci(1)
    assert result == 1
