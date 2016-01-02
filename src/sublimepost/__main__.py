from tygs import WebApp


app, http = WebApp.quickstart('sublimepost')


@http.get('/')
async def hello(req, res):
    res.render('hello.html', {'name': 'world'})


@http.get('/<name>')
async def toto(req, res):
    res.render('hello.html', req.url_params)

if __name__ == '__main__':
    app.ready()
