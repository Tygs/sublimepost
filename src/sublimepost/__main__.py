from tygs import WebApp


app, http = WebApp.quickstart('sublimepost')


@http.get('/')
async def hello(req, res):
    return res.template('hello.html', {'name': 'world'})


@http.get('/<name>')
async def toto(req, res):
    return res.template('hello.html', req.url_params)

if __name__ == '__main__':
    app.ready()
