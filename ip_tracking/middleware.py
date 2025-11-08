from django.http import JsonResponse
from .models import RequestLog, BlockedIP


def fetch_ip(request):
    """
    This function fetches the ip address from
    the request passed as argument
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    else:
        return request.META.get('REMOTE_ADDR')


class IPTrackingMiddleware:
    """
    This middleware logs the IP address, timestamp,
    and path of every incoming request
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Fetch ip and path
        path = request.path
        ip = fetch_ip(request)

        # Log ip and path to database
        request_log = RequestLog(ip_address=ip, path=path)
        request_log.save()

        response = self.get_response(request)

        return response


class BlockedIPMiddleware:
    """
    This middleware rejects requests from users
    on the blocked ip list
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = fetch_ip(request)

        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            return JsonResponse(
                {"message": "IP address is blocked"}, status=403)

        response = self.get_response(request)

        return response
