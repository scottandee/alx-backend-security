from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


@api_view(http_method_names=['GET'])
@renderer_classes([JSONRenderer])
def welcome(request):
    return Response({"message": "Welcome to IP Tracking"})


