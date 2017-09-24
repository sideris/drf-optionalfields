Usage
-----

.. code-block:: bash

    GET http://localhost/models/

    HTTP/1.1 200 OK
    ...
    [
      {
        "a": "val1",
        "b": "val2",
      },
      {
        "a": "valA",
        "b": "valB",
      }
    ]


    GET http://localhost/models/?fields=c

    HTTP/1.1 200 OK
    ...
    [
      {
        "a": "val1",
        "b": "val2",
        "c": "val3"
      },
      {
        "a": "valA",
        "b": "valB",
        "c": "valC",
      }
    ]


    GET http://localhost/models/?fields=c&filter=c

    HTTP/1.1 200 OK
    ...
    [
      {
        "c": "val3"
      },
      {
        "c": "valC",
      }
    ]

.. code-block:: python
    # You can change the field name by extending the mixin
    class MyOptionalFieldsMixin(OptionalFieldsMixin):
        exclude_argument = "some_other_parameter"

    class MyDynamicFilterMixin(DynamicFilterMixin):
        include_argument = "my_filter"



