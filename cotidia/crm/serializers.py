from rest_framework import serializers


class EnquirySerializer(serializers.Serializer):

    name = serializers.CharField(label="Name")
    email = serializers.EmailField(label="Email address")
    message = serializers.CharField(label="Message")

    class Meta:
        fields = (
            'name',
            'email',
            'message',
        )
