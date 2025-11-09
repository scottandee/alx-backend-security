from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django_ratelimit.decorators import ratelimit


@api_view(http_method_names=['GET'])
@renderer_classes([JSONRenderer])
def welcome(request):
    return Response({"message": "Welcome to IP Tracking"})


@api_view(http_method_names=['GET'])
@renderer_classes([JSONRenderer])
@ratelimit(
    key='user_or_ip',
    rate=lambda group, req: ("10/m" if req.user.is_authenticated else "5/m"),
    block=True,
)
def sensitive_view(request):
    return Response({"message": "You're logged in!"})
