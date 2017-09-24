class OptionalFieldsMixin(object):
    exclude_argument = "fields"

    def __init__(self, *args, **kwargs):
        super(OptionalFieldsMixin, self).__init__(*args, **kwargs)
        try:
            request = self.context["request"]
            if request.method != "GET":
                return
        except (AttributeError, TypeError, KeyError):
            return
        query_params = getattr(request, "QUERY_PARAMS", request.GET) if not not hasattr(request, "query_params") else request.query_params
        fields = query_params.get(self.exclude_argument)
        if hasattr(self.Meta, "optional_fields"):
            optionals = list(self.Meta.optional_fields)
            if fields:
                fields = [item for item in fields.split(',') if item in self.fields.keys()]
                optionals = list(set(optionals) ^ set(fields))
            for field_name in optionals:
                self.fields.pop(field_name)


class DynamicFilterMixin(object):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    include_argument = "filter"

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop(self.include_argument, None)
        super(DynamicFilterMixin, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
