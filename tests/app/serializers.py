from rest_framework import serializers

from drf_optionalfields import OptionalFieldsMixin, DynamicFilterMixin
from tests.app.models import Snippet


class SnippetSerializer(OptionalFieldsMixin, DynamicFilterMixin, serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = "__all__"
        optional_fields = ("code", )


