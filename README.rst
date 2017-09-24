Django REST framework OptionalFields
=====================================

drf-optionalfields gives you the flexibility to specify which fields you want to serialized.

There are two mixins available:
`OptionalFieldsMixin`: Which allows you to set some optional fields. These fields can be requested via GET params
`DynamicFilterMixin`: Which allows you to specify only the fields you need.


.. code-block:: python

    from rest_framework.serializers import ModelSerializer
    from drf_optionalfields import OptionalFieldsMixin

    class MyModelSerializer(OptionalFieldsMixin, ModelSerializer):
        class Meta:
            model = SomeModel
            fields = ("id", "username", "address", "full_name")
            optional_fields = ("address", "full_name")
    # or combined with DynamicFilterMixin
    class MyModelSerializer(OptionalFieldsMixin, DynamicFilterMixin, ModelSerializer):
        class Meta:
            model = SomeModel
            fields = ("id", "username", "address", "full_name")
            optional_fields = ("address", "full_name")


.. code-block::

    # You want to see an "address" you have set in the Meta:
    GET /users/1/?fields=address

    # You want only to return "username":
    GET /users/1/?filter=username

    # You want only to return the optional "full_name":
    GET /users/1/?fields=full_name&filter=username


Thanks to Wim Glen for providing great bootstrap code with <https://github.com/wimglenn/djangorestframework-queryfields>(djangorestframework-queryfields)
