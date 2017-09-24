Quickstart
----------

Specify your base model serializer like this:

.. code-block:: python

    from rest_framework.serializers import ModelSerializer
    from drf_optionalfields import OptionalFieldsMixin

    class MyModelSerializer(OptionalFieldsMixin, ModelSerializer):
        class Meta:
            model = SomeModel
            fields = ("a", "b", "c", "d")
            optional_fields = ("c", "d")


This can be mixed with the DynamicFilterMixin as such

.. code-block:: python

    from rest_framework.serializers import ModelSerializer
    from drf_optionalfields import OptionalFieldsMixin

    class MyModelSerializer(OptionalFieldsMixin, DynamicFilterMixin, ModelSerializer):
        class Meta:
            model = SomeModel
            fields = ("a", "b", "c", "d")
            optional_fields = ("c", "d")