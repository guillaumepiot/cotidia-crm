from django.urls import reverse

from cotidia.crm.conf import settings


def admin_menu(context):
    menu_list = []

    if settings.CRM_ENABLE_ACTION:
        menu_list.append({
            "text": "Actions",
            "url": reverse("crm-admin:action-list"),
            "permissions": ["crm.add_action", "crm.change_action"],
        })
    if settings.CRM_ENABLE_CONTACT:
        menu_list.append({
            "text": "Contacts",
            "url": reverse("crm-admin:contact-list"),
            "permissions": ["crm.add_contact", "crm.change_contact"],
        })
    if settings.CRM_ENABLE_ENQUIRY:
        menu_list.append({
            "text": "Enquiries",
            "url": reverse("crm-admin:enquiry-list"),
            "permissions": ["crm.add_enquiry", "crm.change_enquiry"],
        })
    return menu_list
