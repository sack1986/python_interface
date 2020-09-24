# test_simple.py
import requests

def test_one():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 201
