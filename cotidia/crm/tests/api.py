from django.urls import reverse
from django.core import mail

from rest_framework import status
from rest_framework.test import APITestCase

from cotidia.account.doc import Doc
from cotidia.crm.conf import settings


class EnquiryTests(APITestCase):

    fixtures = []

    URLS = {
        'send': 'crm-api:enquiry-send',
    }

    display_doc = True

    def setUp(self):
        self.doc = Doc()

    def test_send(self):
        """Test if we can save an inquiry."""

        url = reverse(self.URLS['send'])

        data = {
            'name': "John Crimson",
            'email': "john@crimson.com",
            'message': "Hello!"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['message'], data['message'])

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Test that the reply email is the one from the user
        self.assertEqual(
            mail.outbox[0].reply_to,
            [settings.CRM_ENQUIRY_REPLY_TO_EMAIL]
        )

        if self.display_doc:
            content = {
                'title': "Send enquiry",
                'http_method': 'POST',
                'url': url,
                'payload': data,
                'response': response.data,
            }
            self.doc.display_section(content)
