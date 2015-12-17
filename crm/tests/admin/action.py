from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from account.models import User
from crm.models import Action

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
        self.object = Action.objects.create(
            attr="test"
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

        # Send data
        data = {
            'attr': 'value'
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Action.objects.filter().latest('id')
        self.assertEqual(obj.attr, 'value')


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

        # Send data
        data = {
            'attr': 'other value'
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Action.objects.get(id=self.object.id)
        self.assertEqual(obj.attr, 'other value')

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
