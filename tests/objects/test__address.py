"""unittest address.py"""

import pytest
from pytest_mock import MockerFixture
from requests import Session

from fortigate_api import FortigateAPI
from tests import helper__tst as tst


@pytest.fixture
def obj():
    """Init FortigateAPI"""
    api = FortigateAPI(host="host")
    api.rest._session = Session()
    return api.address


@pytest.fixture
def connectors():
    """Init Connector objects."""
    api = FortigateAPI(host="host")
    api.rest._session = Session()
    items = [
        api.address,
        api.address_group,
    ]
    return items


@pytest.mark.parametrize("data, expected", [
    ({"name": "NAME1"}, 200),  # already exist
    ({"name": "NAME2"}, 200),  # not exist
    ({"name": "A/B"}, 200),  # already exist
    ({"typo": "NAME1"}, KeyError),
])
def test__create(connectors: list, mocker: MockerFixture, data, expected):
    """Address.create()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.post",
                 side_effect=lambda *args, **kw: tst.session_post(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, int):
            response = connector.create(data)
            actual = response.status_code
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.create(data)


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "NAME1"}, 200),
    ({"uid": "NAME2"}, 404),
    ({"filter": "name==NAME1"}, 200),
    ({"filter": "name==NAME2"}, 200),
    ({"filter": "name==NAME3"}, 200),
    ({"uid": ""}, ValueError),
    ({"uid": "NAME1", "filter": "name==NAME1"}, KeyError),
])
def test__delete(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Address.delete()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.delete",
                 side_effect=lambda *args, **kw: tst.session_delete(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, int):
            response = connector.delete(**kwargs)
            actual = response.status_code
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.delete(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    (dict(uid="NAME1"), ["NAME1"]),
    (dict(uid="NAME1", filter=f"name==NAME1"), ["NAME1"]),
    (dict(uid="NAME2"), []),
    (dict(uid="A/B"), ["A/B"]),
    (dict(filter="name==NAME2"), []),
    (dict(filter=f"name==NAME1"), ["NAME1"]),
    (dict(id="NAME1"), KeyError),
])
def test__get(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Address.get()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        if isinstance(expected, list):
            items = connector.get(**kwargs)
            actual = [d["name"] for d in items]
            assert actual == expected
        else:
            with pytest.raises(expected):
                connector.get(**kwargs)


@pytest.mark.parametrize("kwargs, expected", [
    ({"uid": "NAME1", "data": {"name": "NAME1"}}, 200),
    ({"uid": "NAME3", "data": {"name": "NAME3"}}, 404),
    ({"data": {"name": "NAME1"}}, 200),
    ({"data": {"name": "NAME3"}}, 404),
])
def test__update(connectors: list, mocker: MockerFixture, kwargs, expected):
    """Address.update()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))
    mocker.patch("requests.Session.put",
                 side_effect=lambda *args, **kw: tst.session_put(mocker, *args, **kw))

    for connector in connectors:
        response = connector.update(**kwargs)
        actual = response.status_code
        assert actual == expected


@pytest.mark.parametrize("uid, expected", [
    ("NAME1", True),
    ("NAME3", False),
])
def test__is_exist(connectors: list, mocker: MockerFixture, uid, expected):
    """Address.is_exist()"""
    mocker.patch("requests.Session.get",
                 side_effect=lambda *args, **kw: tst.session_get(mocker, *args, **kw))

    for connector in connectors:
        actual = connector.is_exist(uid=uid)
        assert actual == expected
