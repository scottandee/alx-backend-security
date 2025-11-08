from django.db import models

class RequestLog(models.Model):
    ip_address = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=100)
