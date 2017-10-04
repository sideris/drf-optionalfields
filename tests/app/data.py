# coding: utf-8
from django.http import Http404
from mock_django.query import QuerySetMock

from tests.app.models import Explosive
from tests.app.models import Quote
from tests.app.models import Snippet


def get_snippet_queryset():
    s1 = Snippet(id=1, title='Fork bomb', code=':(){ :|: & };:', language='bash')
    s2 = Snippet(id=2, title='French flag', code="print((u'\x1b[3%s;1m\u2588'*78+u'\n')%((4,)*26+(7,)*26+(1,)*26)*30)")
    snippets_qs = QuerySetMock(Snippet, s1, s2)
    return snippets_qs


def get_snippet_model_instance(pk=None):
    if int(pk) != 3:
        raise Http404
    code = '[ $[ $RANDOM % 6 ] == 0 ] && rm -rf / || echo "click"'
    snippet = Snippet(id=3, title='Russian roulette', code=code, language='bash')
    return snippet
