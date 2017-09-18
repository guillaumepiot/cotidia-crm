import json

from django.db import transaction
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from cotidia.crm.models import Enquiry
from cotidia.crm.serializers import EnquirySerializer
from cotidia.crm.notices import EnquiryNotice
from cotidia.crm.conf import settings


class EnquirySend(APIView):
    """A public api views to save an enquiry."""

    authentication_classes = ()
    permission_classes = ()

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        serializer = EnquirySerializer(data=request.data)

        if serializer.is_valid():
            data = JSONRenderer().render(serializer.data)
            obj = Enquiry.objects.create(data=data)

            data_json = json.loads(data)

            data_json['enquiry_url'] = reverse(
                'crm-admin:enquiry-detail',
                kwargs={'pk': obj.id}
            )

            if not settings.CRM_ENQUIRY_FROM_EMAIL:
                raise Exception(
                    "CRM_ENQUIRY_FROM_EMAIL not set. Must be a string."
                )
            if not settings.CRM_ENQUIRY_REPLY_TO_EMAIL:
                raise Exception(
                    "CRM_ENQUIRY_REPLY_TO_EMAIL not set. Must be a string."
                )
            if not settings.CRM_ENQUIRY_RECIPIENTS:
                raise Exception(
                    "CRM_ENQUIRY_RECIPIENTS not set. Must be a list."
                )

            sender = settings.CRM_ENQUIRY_FROM_EMAIL
            reply_to = settings.CRM_ENQUIRY_REPLY_TO_EMAIL
            subject = settings.CRM_ENQUIRY_SUBJECT
            recipients = settings.CRM_ENQUIRY_RECIPIENTS

            notice = EnquiryNotice(
                subject=subject,
                sender=sender,
                reply_to=reply_to,
                recipients=recipients,
                context=data_json,
                content_object=obj
            )
            # Send the notice straight away
            notice.send()

            data = {
                "message": "Message sent.",
                "data": serializer.data
            }

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
