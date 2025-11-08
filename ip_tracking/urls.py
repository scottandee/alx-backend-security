from django.urls import path
from .views import welcome


urlpatterns = [
    path('', view=welcome),
    path('welcome/', view=welcome),
]