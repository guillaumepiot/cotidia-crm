Cotidia CRM
===========

A CRM that integrates with the Cotidia admin.

	$ pip install -e git+https://guillaumepiot@bitbucket.org/guillaumepiot/cotidia-crm.git#egg=crm

## Commands

Generate random contact using a limit (eg: 50):

	$ python manage.py generate_contacts 50

Flush all contacts (permanently remove from the database):

	$ python manage.py flush_contacts

## Tests

Always run the tests:
	
	$ python manage.py test crm.tests

Also, make sure the tests are added the deployment scripts (`fabfile.py`).