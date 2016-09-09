from django.db import transaction
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from crm.serializers import EnquirySerializer
from crm.notices import EnquiryNotice
from crm.settings import ENQUIRY_RECIPIENTS


class EnquirySend(APIView):
    """A public api views to save an enquiry."""

    authentication_classes = ()
    permission_classes = ()

    @transaction.atomic
    def post(self, request):

        serializer = EnquirySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            instance = serializer.instance

            # Flatten the serializer data
            data = serializer.data

            data['enquiry_url'] = reverse(
                'crm-admin:enquiry-detail',
                kwargs={'pk': instance.id}
                )
            sender = '%s <%s>' % (data['full_name'], data['email'])

            subject = "New website inquiry"

            notice = EnquiryNotice(
                subject=subject,
                sender=sender,
                reply_to=[data['email']],
                recipients=ENQUIRY_RECIPIENTS,
                context=data,
                content_object=instance
            )
            # Send the notice straight away
            notice.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
