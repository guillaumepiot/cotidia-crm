from cotidia.crm import settings


def crm_settings(request):

    return {
        "ENABLE_ACTION": settings.ENABLE_ACTION,
        "ENABLE_CONTACT": settings.ENABLE_CONTACT,
        "ENABLE_ENQUIRY": settings.ENABLE_ENQUIRY,
    }
