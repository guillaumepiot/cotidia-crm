from django.conf import settings

from cotimail.notice import Notice

class EnquiryNotice(Notice):
    # Use as a list display
    name = 'New enquiry' 
    # Use for the preview URL as a slug, so it must not contains 
    # spaces or other symbols than lowercase letters and hyphens
    identifier = 'new-enquiry' 
    # Defines an HTML template for this notice
    html_template = 'notification/new_enquiry.html'
    text_template = 'notification/new_enquiry.txt'

    # A context passed to every request (merge with `context`)
    default_context = {
        'SITE_URL': settings.SITE_URL
    }

    # A JSON representation of the context dictionary, 
    #which is the format it will be saved as in the EmailLog
    context = {  
        "full_name":"Guillaume Piot",
        "email":"guillaume@piot.co.uk",
        "message":"Hello!",
        "enquiry_url": "/admin/crm/enquiry/21/"
    }

    # Passing on come context variables to build the subject line 
    subject = 'New inquiry'