from django.urls import path, include

urlpatterns = [
    path('ip-tracking/', include('ip_tracking.urls')),
]
