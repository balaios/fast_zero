from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_ola_deve_retornar_ok_e_ola_mundo_html(client):
    response = client.get('/ola')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title>Olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo! </h1>
      </body>
    </html>"""
    )
