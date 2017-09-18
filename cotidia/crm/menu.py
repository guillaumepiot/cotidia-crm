# {% load i18n %}
# <div class="menu__section-header">
#     {% trans "CRM" %}
# </div>
# {% if perms.crm.change_action and ENABLE_ACTION %}
# <a href="{% url 'crm-admin:action-list' %}" class="[ menu__item ] [ menu-item ]">
#     <span class="menu-item__icon fa fa-check-square"></span>
#     <span class="menu-item__text">{% trans "Actions" %}</span>
# </a>
# {% endif %}
# {% if perms.crm.change_contact and ENABLE_CONTACT %}
# <a href="{% url 'crm-admin:contact-list' %}" class="[ menu__item ] [ menu-item ]">
#     <span class="menu-item__icon fa fa-users"></span>
#     <span class="menu-item__text">{% trans "Contacts" %}</span>
# </a>
# {% endif %}
# {% if perms.crm.change_enquiry and ENABLE_ENQUIRY %}
# <a href="{% url 'crm-admin:enquiry-list' %}" class="[ menu__item ] [ menu-item ]">
#     <span class="menu-item__icon fa fa-envelope"></span>
#     <span class="menu-item__text">{% trans "Enquiries" %}</span>
# </a>
# {% endif %}

from django.core.urlresolvers import reverse

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
