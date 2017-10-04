from rest_framework import viewsets

from tests.app.data import get_snippet_model_instance
from tests.app.data import get_snippet_queryset
from tests.app.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):

    serializer_class = SnippetSerializer

    def get_queryset(self):
        return get_snippet_queryset()

    def get_object(self):
        pk = self.request.parser_context['kwargs']['pk']
        return get_snippet_model_instance(pk=pk)

