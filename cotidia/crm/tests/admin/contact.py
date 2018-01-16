from django.test import TestCase, Client
from django.urls import reverse

from cotidia.account.models import User
from cotidia.crm.models import Contact


class ContactTests(TestCase):

    def setUp(self):
        # Create a super user
        self.user = User.objects.create(
            username="admin",
            email="admin@test.com",
            is_superuser=True,
            is_active=True)
        self.user.set_password("demo")
        self.user.save()

        # Create a default object, to use with update, retrieve, list & delete
        self.object = Contact.objects.create(
            title="mr",
            first_name="Guillaume",
            last_name="Piot",
        )

        # Create the client and login the user
        self.c = Client()
        self.c.login(username=self.user.username, password='demo')

    def test_add_contact(self):
        """Test that we can add a new object."""

        url = reverse('crm-admin:contact-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'title': "mr",
            'first_name': "Guillaume",
            'last_name': "Piot",
            'job': "Director",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Contact.objects.filter().latest('id')
        self.assertEqual(obj.title, 'mr')
        self.assertEqual(obj.first_name, 'Guillaume')
        self.assertEqual(obj.last_name, 'Piot')
        self.assertEqual(obj.job, 'Director')

    def test_update_contact(self):
        """Test that we can update an existing object."""

        url = reverse(
            'crm-admin:contact-update',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'title': "ms",
            'first_name': "Kate",
            'last_name': "Smith",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Contact.objects.get(id=self.object.id)
        self.assertEqual(obj.title, 'ms')
        self.assertEqual(obj.first_name, 'Kate')
        self.assertEqual(obj.last_name, 'Smith')

    def test_retrieve_contact(self):
        """Test that we can retrieve an object from its ID."""

        url = reverse(
            'crm-admin:contact-detail',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_contact(self):
        """Test that we can list objects."""

        url = reverse('crm-admin:contact-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_contact(self):
        """Test that we can delete an object."""

        url = reverse(
            'crm-admin:contact-delete',
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
        obj = Contact.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
