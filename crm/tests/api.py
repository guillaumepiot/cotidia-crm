import os, datetime

from django.core.urlresolvers import reverse
from django.conf import settings
from django.core import mail

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from crm.models import Enquiry

URLS = {
    'send': 'crm-api:enquiry-send',
}

class EnquiryTests(APITestCase):
    
    fixtures = []

    def setUp(self):
        pass

    def test_send(self):

        """ Test if we can save an inquiry """
   
        url = reverse(URLS['send'])

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
