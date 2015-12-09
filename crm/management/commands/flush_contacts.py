import names
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from crm.models import Contact


class Command(BaseCommand):
    args = ''
    help = 'Delete all contacts'

    def handle(self, *args, **options):
        Contact.objects.all().delete()