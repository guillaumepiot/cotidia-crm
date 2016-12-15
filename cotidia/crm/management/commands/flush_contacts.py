from django.core.management.base import BaseCommand
from crm.models import Contact


class Command(BaseCommand):
    args = ''
    help = 'Delete all contacts'

    def handle(self, *args, **options):
        Contact.objects.all().delete()
