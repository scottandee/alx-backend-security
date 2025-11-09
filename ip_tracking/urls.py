from django.urls import path
from .views import welcome, sensitive_view


urlpatterns = [
    path('welcome/', view=welcome),
    path('sensitive/', view=sensitive_view),
]
