import names, random
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from crm.models import Contact

def phn():
    p=list('0000000000')
    p[0] = str(random.randint(1,9))
    for i in [1,2,6,7,8]:
        p[i] = str(random.randint(0,9))
    for i in [3,4]:
        p[i] = str(random.randint(0,8))
    if p[3]==p[4]==0:
        p[5]=str(random.randint(1,8))
    else:
        p[5]=str(random.randint(0,8))
    n = range(10)
    if p[6]==p[7]==p[8]:
        n = (i for i in n if i!=p[6])
    p[9] = str(random.choice(n))
    p = ''.join(p)
    return p[:3] + '-' + p[3:6] + '-' + p[6:]

class Command(BaseCommand):
    args = '<limit>'
    help = 'Generate <limit> random contacts'

    def handle(self, *args, **options):
        
        if not len(args) == 1:
            raise CommandError("Please provide limit number")

        for i in range(0, int(args[0])):
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            email = "%s.%s@example.com" % (first_name.lower(), last_name.lower())
            phone_number = phn()
            Contact.objects.create(
                title="mr",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number
                )