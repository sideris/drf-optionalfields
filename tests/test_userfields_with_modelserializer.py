from rest_framework.test import APIClient

from tests.utils import decode_content


def test_response_without_fields():
    response = APIClient().get('/snippets/')
    expected = [
        {
            'id': 1,
            'title': 'Fork bomb',
            'linenos': False,
            'language': 'bash',
        },
        {
            'id': 2,
            'title': 'French flag',
            'linenos': False,
            'language': 'python',
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_response_with_fields():
    response = APIClient().get('/snippets/?fields=code')
    expected = [
        {
            'id': 1,
            'title': 'Fork bomb',
            'code': ':(){ :|: & };:',
            'linenos': False,
            'language': 'bash',
        },
        {
            'id': 2,
            'title': 'French flag',
            'code': "print((u'\x1b[3%s;1m\u2588'*78+u'\n')%((4,)*26+(7,)*26+(1,)*26)*30)",
            'linenos': False,
            'language': 'python',
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_response_with_filter():
    response = APIClient().get('/snippets/?filter=title')
    expected = [
        {
            'title': 'Fork bomb',
        },
        {
            'title': 'French flag',
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_response_with_fields_and_filter():
    response = APIClient().get('/snippets/?fields=code&filter=code')
    expected = [
        {
            'code': ':(){ :|: & };:',
        },
        {
            'code': "print((u'\x1b[3%s;1m\u2588'*78+u'\n')%((4,)*26+(7,)*26+(1,)*26)*30)",
        },
    ]
    content = decode_content(response)
    assert content == expected

