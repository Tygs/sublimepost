from tygs import WebApp


app, http = WebApp.quickstart('sublimepost')


@http.get('/')
async def hello(req, res):
    res.render('hello', {'name': 'world'})

app.ready()
