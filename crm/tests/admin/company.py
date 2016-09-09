from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from account.models import User
from crm.models import Company


class CompanyTests(TestCase):

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
        self.object = Company.objects.create(
            name="Test company"
            )

        # Create the client and login the user
        self.c = Client()
        self.c.login(username=self.user.username, password='demo')

    def test_add_company(self):
        """Test that we can add a new object."""

        url = reverse('crm-admin:company-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'name': 'Test company'
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Company.objects.filter().latest('id')
        self.assertEqual(obj.name, 'Test company')

    def test_update_company(self):
        """Test that we can update an existing object."""

        url = reverse(
            'crm-admin:company-update',
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'name': 'Other company'
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Company.objects.get(id=self.object.id)
        self.assertEqual(obj.name, 'Other company')

    def test_retrieve_company(self):
        """Test that we can retrieve an object from its ID."""

        url = reverse(
            'crm-admin:company-detail',
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_company(self):
        """Test that we can list objects."""

        url = reverse('crm-admin:company-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_company(self):
        """Test that we can delete an object."""

        url = reverse(
            'crm-admin:company-delete',
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
        obj = Company.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
