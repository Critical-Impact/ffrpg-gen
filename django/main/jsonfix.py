from rest_framework.renderers import JSONRenderer
from rest_framework import pagination, serializers

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {}

        #determine the resource name for this request - default to objects if not defined
        if "get_serializer" in dir(renderer_context.get('view')):
            resource = getattr(renderer_context.get('view').get_serializer().Meta, 'resource_name', 'objects')
        else:
            resource = 'objects'


        response_data[resource] = data

        #call super to render the response
        response = super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)

        return response

class CustomMetaSerializer(serializers.Serializer):
    next_page = pagination.NextPageField(source='*')
    prev_page = pagination.PreviousPageField(source='*')
    record_count = serializers.Field(source='paginator.count')

class CustomPaginationSerializer(pagination.BasePaginationSerializer):
    # Takes the page object as the source
    meta = CustomMetaSerializer(source='*')
    results_field = 'paginated_results'