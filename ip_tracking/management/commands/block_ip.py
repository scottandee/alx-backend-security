from django.core.management.base import BaseCommand, CommandError
from ip_tracking.models import BlockedIP


class Command(BaseCommand):
    help = 'Adds an IP address to the blocked list'

    def add_arguments(self, parser):
        parser.add_argument('ip_address', type=str, help='IP address to block')

    def handle(self, *args, **options):
        ip_address = options['ip_address']

        # # Raise error if IP is already blocked
        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            raise CommandError('"%s" is already in blocked list' % ip_address)

        # Add IP to blocked list
        blocked_ip = BlockedIP(ip_address=ip_address)
        blocked_ip.save()

        self.stdout.write(
            self.style.SUCCESS('Successfully added "%s"' % ip_address)
        )
