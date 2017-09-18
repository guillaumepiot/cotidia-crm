from django.conf import settings

from appconf import AppConf


class CRMConf(AppConf):

    ENABLE_ACTION = True
    ENABLE_CONTACT = True
    ENABLE_ENQUIRY = True

    ENQUIRY_RECIPIENTS = None  # Must be a list []
    ENQUIRY_FROM_EMAIL = None  # Must be an email
    ENQUIRY_REPLY_TO_EMAIL = None  # Must be an email
    ENQUIRY_SUBJECT = "New website inquiry"

    class Meta:
        prefix = 'crm'
