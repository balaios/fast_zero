from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, todos, users
from fast_zero.schemas import Message

app = FastAPI()

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/ola', response_class=HTMLResponse)
def ola():
    return """
    <html>
      <head>
        <title>Olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo! </h1>
      </body>
    </html>"""
