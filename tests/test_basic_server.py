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
    srv = Server(app)
    t = Process(target=srv.run)
    t.start()
    sleep(1)
    yield
    # srv.stop()
    t.terminate()
    # t.join()


def test_run():
    req = requests.get('http://localhost:8080')
    assert b'Hello world' in req.content

def test_server():
    srv = Server(app)
    srv.loop = MagicMock()
    srv.server = MagicMock()
    srv.app = MagicMock()
    srv.handler = MagicMock()
    c = srv.loop.run_until_complete.call_count
    srv.get_server()
    assert srv.loop.run_until_complete.call_count == c + 1, 'run_until_complete has not been called since server fetch'
    c2 = srv.loop.run_forever.call_count

    srv._run_server()
    assert srv.loop.run_forever.call_count == c2 + 1, 'run_forever has not been called since run call'
    assert srv.loop.close.call_count == 1
    assert srv.server.close.call_count == 1
    assert srv.handler.finish_connections.call_count == 1
    assert srv.app.finish.call_count == 1
