from .models import RequestLog
import logging


class IPTrackingMiddleware:
    """
    This middleware logs the IP address, timestamp,
    and path of every incoming request
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        path = request.path
        ip = ''
        
        # Fetch IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # Log ip and path to database
        request_log = RequestLog(ip_address=ip, path=path)
        request_log.save()
        
        response = self.get_response(request)

        return response



