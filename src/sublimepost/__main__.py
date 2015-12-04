from aiohttp import web
import jinja2
import aiohttp_jinja2
from path import Path

from sublimepost.server import Server


@aiohttp_jinja2.template('hello.jinja2')
async def hello(request):
    return {'name': 'world'}

app = web.Application()
aiohttp_jinja2.setup(app,
                     loader=jinja2.FileSystemLoader(Path(__file__).parent
                                                    / 'templates'))
app.router.add_route('GET', '/', hello)


def main():
    srv = Server(app)
    srv.run()

if __name__ == '__main__':
    main()
