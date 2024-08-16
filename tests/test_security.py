from http import HTTPStatus

import pytest
from fastapi import HTTPException
from jwt import decode

from fast_zero.security import (
    SECRET_KEY,
    create_access_token,
    get_current_user,
)


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_not_user():
    data = {'sub': ''}
    token = create_access_token(data)

    with pytest.raises(HTTPException) as excinfo:
        get_current_user(token=token)
    assert str(excinfo.value) == '401: Could not validate credentials'


def test_get_current_user_invalid(session):
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    with pytest.raises(HTTPException) as excinfo:
        get_current_user(session=session, token=token)
    assert str(excinfo.value) == '401: Could not validate credentials'
