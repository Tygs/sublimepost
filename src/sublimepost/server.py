import asyncio


class Server:

    def __init__(self, app):
        self.loop = asyncio.get_event_loop()
        self.app = app
        self.handler = self.app.make_handler()
        self._server_factory = self.loop.create_server(self.handler, '0.0.0.0',
                                                       8080)
        self.server = None

    def run(self):
        self.server = self.loop.run_until_complete(self._server_factory)
        print('Serving on', self.server.sockets[0].getsockname())
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()

    def stop(self):
        self.loop.run_until_complete(self.handler.finish_connections(1.0))
        self.srv.close()
        self.loop.run_until_complete(self.srv.wait_closed())
        self.loop.run_until_complete(self.app.finish())
        self.loop.close()
