# from threading import Thread
from multiprocessing import Process
from time import sleep

import pytest
import requests

from sublimepost.__main__ import app
from sublimepost.server import Server


@pytest.yield_fixture(scope='session')
def start_server():
    srv = Server(app)
    t = Process(target=srv.run)
    t.start()
    sleep(1)
    yield
    # srv.stop()
    t.terminate()
    # t.join()


def test_run(start_server):
    req = requests.get('http://localhost:8080')
    assert b'Hello world' in req.content
