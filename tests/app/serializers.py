from rest_framework import serializers

from drf_optionalfields import QueryFieldsMixin
from tests.app.fields import BoomField
from tests.app.models import Snippet


class QuoteSerializer(QueryFieldsMixin, serializers.Serializer):

    character = serializers.CharField()
    line = serializers.CharField()
    sketch = serializers.CharField()


class SnippetSerializer(QueryFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Snippet
        exclude = ()


class ExplosiveSerializer(QueryFieldsMixin, serializers.Serializer):

    safe = serializers.CharField()
    boom = BoomField()
