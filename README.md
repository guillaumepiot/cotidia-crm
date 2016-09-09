Cotidia CRM
===========

A CRM that integrates with the Cotidia admin.

    $ pip install -e git+git@code.cotidia.com:cotidia/crm.git#egg=crm

## Setup

Add `crm` to your settings `INSTALLED_APPS`.

Run the migration:

```console
$ python manage.py migrate
```

Include in the context processors:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
                'crm.context_processor.crm_settings',
            ],
        },
    },
]
```
  
Add the CRM urls:

```python
urlpatterns = [
    ...
    url(r'^api/crm/', include('crm.urls.api',
        namespace="crm-api")),
    url(r'^admin/crm/', include('crm.urls.admin',
        namespace="crm-admin")),
    ...
]
```

## Commands

Generate random contact using a limit (eg: 50):

    $ python manage.py generate_contacts 50

Flush all contacts (permanently remove from the database):

    $ python manage.py flush_contacts

## Tests

Always run the tests:
    
    $ python manage.py test crm.tests

Also, make sure the tests are added the deployment scripts (`fabfile.py`).