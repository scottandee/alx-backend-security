from django.db import models


class RequestLog(models.Model):
    ip_address = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=100)


class BlockedIP(models.Model):
    ip_address = models.CharField(max_length=50)
