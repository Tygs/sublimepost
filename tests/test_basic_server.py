from multiprocessing import Process
from time import sleep

import pytest
import requests
from path import Path

import sublimepost
from sublimepost.__main__ import app


@pytest.yield_fixture(scope='module', autouse=True)
def start_server():
    path = Path(sublimepost.__file__).parent
    t = Process(target=app.ready, kwargs={'cwd': path})
    t.start()
    sleep(1)
    yield
    t.terminate()
    t.join()


def test_run(start_server):
    req = requests.get('http://localhost:8080')
    assert b'Hello world' in req.content

    req = requests.get('http://localhost:8080/test')
    assert b'Hello test' in req.content


def test_basic_xss(start_server):
    req = requests.get('http://localhost:8080/<h1>test')
    assert b'Hello &lt;h1&gt;test' in req.content
