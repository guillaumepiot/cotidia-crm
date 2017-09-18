from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from cotidia.account.models import User
from cotidia.crm.models import Note, Contact


class NoteTests(TestCase):

    def setUp(self):
        # Create a super user
        self.user = User.objects.create(
            username="admin",
            email="admin@test.com",
            is_superuser=True,
            is_active=True)
        self.user.set_password("demo")
        self.user.save()

        # Create a new contact
        self.contact = Contact.objects.create(
            title="mr",
            first_name="Steve",
            last_name="Brown")

        # Create a default object, to use with update, retrieve, list & delete
        self.object = Note.objects.create(
            comment="test note",
            contact=self.contact
            )

        # Create the client and login the user
        self.c = Client()
        self.c.login(username=self.user.username, password='demo')

    def test_add_note(self):
        """Test that we can add a new object."""

        url = "{0}?contact={1}".format(
            reverse('crm-admin:note-add'), self.contact.id)

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'comment': 'value'
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Note.objects.filter().latest('id')
        self.assertEqual(obj.comment, 'value')

    def test_update_note(self):
        """Test that we can update an existing object."""

        url = reverse(
            'crm-admin:note-update',
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'comment': 'other value'
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Note.objects.get(id=self.object.id)
        self.assertEqual(obj.comment, 'other value')

    def test_delete_note(self):
        """Test that we can delete an object."""

        url = reverse(
            'crm-admin:note-delete',
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
        obj = Note.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
