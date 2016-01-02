# from threading import Thread
from multiprocessing import Process
from time import sleep
from unittest.mock import MagicMock

import pytest
import requests

from sublimepost.__main__ import app
from sublimepost.server import Server


@pytest.yield_fixture(scope='module', autouse=True)
def start_server():
    print('Before process')
    t = Process(target=app.ready)
    print('After process creation')
    t.start()
    print('After process start')
    sleep(3)
    print('After slip')
    yield
    print('After yield')
    # srv.stop()
    t.terminate()
    print('After terminate')
    t.join()
    print('After join')


def test_run():
    req = requests.get('http://localhost:8080')
    assert b'Hello world' in req.content
