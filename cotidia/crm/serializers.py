from rest_framework import serializers

from cotidia.crm.models import Enquiry


class EnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Enquiry
        fields = (
            'full_name',
            'email',
            'message'
            )
