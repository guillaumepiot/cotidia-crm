import datetime
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from account.models import User
from crm.models import Action, Contact

class ActionTests(TestCase):

    def setUp(self):
        """
        The set up function get executed before each test. Any non-testing data
        used across all tests should be created here.
        Eg:
        self.default_data = {}
        """

        # Create a super user
        self.user = User.objects.create(
            username="admin",
            email="admin@test.com",
            is_superuser=True,
            is_active=True)
        self.user.set_password("demo")
        self.user.save()

        # Create a default object, to use with update, retrieve, list & delete
        self.contact = Contact.objects.create(
            title="mr",
            first_name="Guillaume",
            last_name="Piot",
            )

        # Create a default object, to use with update, retrieve, list & delete
        self.object = Action.objects.create(
            title="Action title",
            description="Action description",
            due_date=datetime.datetime.today(),
            due_time=datetime.time(),
            completed=False,
            contact=self.contact
            )

        # Create the client and login the user
        self.c = Client()
        self.c.login(username=self.user.username, password='demo')

    def test_add_action(self):
        """
        Test that we can add a new object
        """

        url = reverse('crm-admin:action-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        today = datetime.datetime.today()
        today = datetime.date(today.year, today.month, today.day)
        now = datetime.time()

        # Send data
        data = {
            'title': "Action title",
            'description': "Action description",
            'due_date_day': today.day,
            'due_date_month': today.month,
            'due_date_year': today.year,
            'due_time_hour': now.hour,
            'due_time_minute': now.minute,
            'completed': True,
            'contact': self.contact.id
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)


        # Get the latest added object
        obj = Action.objects.filter().latest('id')
        self.assertEqual(obj.title, "Action title")
        self.assertEqual(obj.description, "Action description")
        self.assertEqual(obj.due_date, today)
        self.assertEqual(obj.due_time, now)
        self.assertEqual(obj.completed, True)
        self.assertEqual(obj.contact, self.contact)
        

    def test_update_action(self):
        """
        Test that we can update an existing object
        """

        url = reverse('crm-admin:action-update', 
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        today = datetime.datetime.today()
        today = datetime.date(today.year, today.month, today.day)
        now = datetime.time()

        # Send data
        data = {
            'title': 'Other title',
            'description': "Action description",
            'due_date_day': today.day,
            'due_date_month': today.month,
            'due_date_year': today.year,
            'due_time_hour': now.hour,
            'due_time_minute': now.minute,
            'completed': True,
            'contact': self.contact.id
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Action.objects.get(id=self.object.id)
        self.assertEqual(obj.title, 'Other title')

    def test_retrieve_action(self):
        """
        Test that we can retrieve an object from its ID
        """

        url = reverse('crm-admin:action-detail', 
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_action(self):
        """
        Test that we can list objects
        """

        url = reverse('crm-admin:action-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_action(self):
        """
        Test that we can delete an object
        """

        url = reverse('crm-admin:action-delete', 
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Action detail with POST call
        response = self.c.post(url)
        self.assertEqual(response.status_code, 302)

        # Test that the record has been deleted
        obj = Action.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
