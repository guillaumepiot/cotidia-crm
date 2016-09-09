from django.core.urlresolvers import reverse
from django.core import mail

from rest_framework import status
from rest_framework.test import APITestCase

from account.doc import Doc


class EnquiryTests(APITestCase):

    fixtures = []

    URLS = {
        'send': 'crm-api:enquiry-send',
    }

    def setUp(self):
        self.doc = Doc()

    def test_send(self):
        """Test if we can save an inquiry."""

        url = reverse(self.URLS['send'])

        data = {
            'full_name': "John Crimson",
            'email': "john@crimson.com",
            'message': "Hello!"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], "John Crimson")
        self.assertEqual(response.data['email'], "john@crimson.com")
        self.assertEqual(response.data['message'], "Hello!")

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Test that the reply email is the one from the user
        self.assertEqual(mail.outbox[0].reply_to, ["john@crimson.com"])

        # Generate documentation
        content = {
            'title': "Send enquiry",
            'http_method': 'POST',
            'url': url,
            'payload': data,
            'response': response.data,
        }
        self.doc.display_section(content)
