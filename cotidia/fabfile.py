# Run as local
import sys, random
from fabric.api import *
from os.path import exists

def add_module():
    prompt('Specify exiting app name:', 'app_name', validate=r'^[a-z\_]+$')
    prompt('Specify new module name (model class name):', 'module_name', validate=r'^[a-zA-Z\_]+$')

    with settings(warn_only=True):

        # Rename the project folder
        if local("cd %s" % env.app_name).failed:
            print("!!! App name does not exist !!! - Use python manage.py startapp to create a new app")

        #
        # Add the tests
        #
        if local("cd %s/tests" % env.app_name).failed:
            local("mkdir %s/tests"% env.app_name)

        if local('echo "from .admin import *\nfrom .public import *" > %s/tests/__init__.py' % env.app_name).failed:
            local("touch %s/tests/__init__.py"% env.app_name)

        if local("cd %s/tests/admin" % env.app_name).failed:
            local("mkdir %s/tests/admin"% env.app_name)

        if local("cat %s/tests/admin/__init__.py" % env.app_name).failed:
            local("touch %s/tests/admin/__init__.py"% env.app_name)

        if local("cd %s/tests/public" % env.app_name).failed:
            local("mkdir %s/tests/public"% env.app_name)

        if not exists("%s/tests/public/__init__.py" % env.app_name):
            local("touch %s/tests/public/__init__.py"% env.app_name)

        if not exists("%s/tests/admin/%s.py" % (env.app_name, env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/tests.py > %s/tests/admin/%s.py' \
                % (env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/from app.models import Model/from %s.models import %s/g' %s/tests/admin/%s.py" % \
            (env.app_name, env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelTests/%sTests/g' %s/tests/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/_model/_%s/g' %s/tests/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-admin/%s-admin/g' %s/tests/admin/%s.py" % \
            (env.app_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-admin/%s-admin/g' %s/tests/admin/%s.py" % \
            (env.app_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/model-add/%s-add/g' %s/tests/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-update/%s-update/g' %s/tests/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-detail/%s-detail/g' %s/tests/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-list/%s-list/g' %s/tests/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-delete/%s-delete/g' %s/tests/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/Model./%s./g' %s/tests/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("rm %s/tests/admin/%s.py.bak" % (env.app_name, env.module_name.lower()))

        #
        # Add the URLs
        #
        if local("cd %s/urls" % env.app_name).failed:
            local("mkdir %s/urls"% env.app_name)

        if local("cat %s/urls/__init__.py" % env.app_name).failed:
            local("touch %s/urls/__init__.py"% env.app_name)

        if local("cd %s/urls/admin" % env.app_name).failed:
            local("mkdir %s/urls/admin"% env.app_name)

        if local("cat %s/urls/admin/__init__.py" % env.app_name).failed:
            local("touch %s/urls/admin/__init__.py"% env.app_name)

        if local("cd %s/urls/public" % env.app_name).failed:
            local("mkdir %s/urls/public"% env.app_name)

        if not exists("%s/urls/public/__init__.py" % env.app_name):
            local("touch %s/urls/public/__init__.py"% env.app_name)

        if not exists("%s/urls/admin/%s.py" % (env.app_name, env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/urls.py > %s/urls/admin/%s.py' \
                % (env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/from app.views.admin import/from %s.views.admin.%s import/g' %s/urls/admin/%s.py" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/model-add/%s-add/g' %s/urls/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-update/%s-update/g' %s/urls/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-detail/%s-detail/g' %s/urls/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-list/%s-list/g' %s/urls/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-delete/%s-delete/g' %s/urls/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/ModelCreate/%sCreate/g' %s/urls/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelUpdate/%sUpdate/g' %s/urls/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelDetail/%sDetail/g' %s/urls/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelList/%sList/g' %s/urls/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelDelete/%sDelete/g' %s/urls/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/Model management/%s management/g' %s/urls/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("rm %s/urls/admin/%s.py.bak" % (env.app_name, env.module_name.lower()))

        #
        # Add the Views
        #
        if local("cd %s/views" % env.app_name).failed:
            local("mkdir %s/views"% env.app_name)

        if local("cat %s/views/__init__.py" % env.app_name).failed:
            local("touch %s/views/__init__.py"% env.app_name)

        if local("cd %s/views/admin" % env.app_name).failed:
            local("mkdir %s/views/admin"% env.app_name)

        if local("cat %s/views/admin/__init__.py" % env.app_name).failed:
            local("touch %s/views/admin/__init__.py"% env.app_name)

        if local("cd %s/views/public" % env.app_name).failed:
            local("mkdir %s/views/public"% env.app_name)

        if not exists("%s/views/public/__init__.py" % env.app_name):
            local("touch %s/views/public/__init__.py"% env.app_name)

        if not exists("%s/views/admin/%s.py" % (env.app_name, env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/views.py > %s/views/admin/%s.py' \
                % (env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/from app.models import Model/from %s.models import %s/g' %s/views/admin/%s.py" % \
            (env.app_name, env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/from app.forms.admin.model/from %s.forms.admin.%s/g' %s/views/admin/%s.py" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/ModelAddForm/%sAddForm/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/model-add/%s-add/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-update/%s-update/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-detail/%s-detail/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-list/%s-list/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model-delete/%s-delete/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/model-admin/%s-admin/g' %s/views/admin/%s.py" % \
            (env.app_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/ModelCreate/%sCreate/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelUpdate/%sUpdate/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelDetail/%sDetail/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelList/%sList/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelDelete/%sDelete/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/Model management/%s management/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/Model/%s/g' %s/views/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/admin\/app\/model/admin\/%s\/%s/g' %s/views/admin/%s.py" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.module_name.lower()))


        local("sed -i .bak 's/model_list/%s_list/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model_detail/%s_detail/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model_form/%s_form/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/model_confirm_delete/%s_confirm_delete/g' %s/views/admin/%s.py" % \
            (env.module_name.lower(), env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/app.change_model/%s.change_%s/g' %s/views/admin/%s.py" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/app.add_model/%s.add_%s/g' %s/views/admin/%s.py" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/app.delete_model/%s.delete_%s/g' %s/views/admin/%s.py" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.module_name.lower()))

        local("rm %s/views/admin/%s.py.bak" % (env.app_name, env.module_name.lower()))

        #
        # Add the Forms
        #
        if local("cd %s/forms" % env.app_name).failed:
            local("mkdir %s/forms"% env.app_name)

        if local("cat %s/forms/__init__.py" % env.app_name).failed:
            local("touch %s/forms/__init__.py"% env.app_name)

        if local("cd %s/forms/admin" % env.app_name).failed:
            local("mkdir %s/forms/admin"% env.app_name)

        if local("cat %s/forms/admin/__init__.py" % env.app_name).failed:
            local("touch %s/forms/admin/__init__.py"% env.app_name)

        if local("cd %s/forms/public" % env.app_name).failed:
            local("mkdir %s/forms/public"% env.app_name)

        if not exists("%s/forms/public/__init__.py" % env.app_name):
            local("touch %s/forms/public/__init__.py"% env.app_name)

        if not exists("%s/forms/admin/%s.py" % (env.app_name, env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/forms.py > %s/forms/admin/%s.py' \
                % (env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/from app.models import Model/from %s.models import %s/g' %s/forms/admin/%s.py" % \
            (env.app_name, env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/MODEL FORMS/%s FORMS/g' %s/forms/admin/%s.py" % \
            (env.module_name.upper(), env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/model = Model/model = %s/g' %s/forms/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/Model\./%s\./g' %s/forms/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("sed -i .bak 's/ModelAddForm/%sAddForm/g' %s/forms/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))
        local("sed -i .bak 's/ModelUpdateForm/%sUpdateForm/g' %s/forms/admin/%s.py" % \
            (env.module_name, env.app_name, env.module_name.lower()))

        local("rm %s/forms/admin/%s.py.bak" % (env.app_name, env.module_name.lower()))

        #
        # Add the Templates
        #
        if local("cd %s/templates" % env.app_name).failed:
            local("mkdir %s/templates"% env.app_name)

        if local("cd %s/templates/admin" % env.app_name).failed:
            local("mkdir %s/templates/admin"% env.app_name)

        if local("cd %s/templates/admin/%s" % (env.app_name, env.app_name)).failed:
            local("mkdir %s/templates/admin/%s"% (env.app_name, env.app_name))

        if local("cd %s/templates/admin/%s/%s" % (env.app_name, env.app_name, env.module_name.lower())).failed:
            local("mkdir %s/templates/admin/%s/%s"% (env.app_name, env.app_name, env.module_name.lower()))

        if not exists("%s/templates/admin/%s/%s/%s_form.html" % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/model_form.html > %s/templates/admin/%s/%s/%s_form.html' \
                % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/Edit Model/Edit %s/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/Add a Model/Add a %s/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Models\"/trans \"%s\"/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Model detail\"/trans \"%s detail\"/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-add/%s-add/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-update/%s-update/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-detail/%s-detail/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-list/%s-list/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-delete/%s-delete/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-admin/%s-admin/g' %s/templates/admin/%s/%s/%s_form.html" % \
            (env.app_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("rm %s/templates/admin/%s/%s/%s_form.html.bak" % \
            (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        if not exists("%s/templates/admin/%s/%s/%s_list.html" % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/model_list.html > %s/templates/admin/%s/%s/%s_list.html' \
                % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Models\"/trans \"%s\"/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Add a model\"/trans \"Add a %s\"/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-add/%s-add/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-update/%s-update/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-detail/%s-detail/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-list/%s-list/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-delete/%s-delete/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-admin/%s-admin/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.app_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/perms.app.add_model/perms.%s.add_%s/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/Add a Model/Add a %s/g' %s/templates/admin/%s/%s/%s_list.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("rm %s/templates/admin/%s/%s/%s_list.html.bak" % \
            (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        if not exists("%s/templates/admin/%s/%s/%s_detail.html" % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/model_detail.html > %s/templates/admin/%s/%s/%s_detail.html' \
                % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Models\"/trans \"%s\"/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/Edit Model/Edit %s/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/Model details/%s details/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/Delete Model/Delete %s/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Model details\"/trans \"%s details\"/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Edit model\"/trans \"Edit %s\"/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-add/%s-add/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-update/%s-update/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-detail/%s-detail/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-list/%s-list/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-delete/%s-delete/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-admin/%s-admin/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.app_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/perms.app.delete_model/perms.%s.delete_%s/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/perms.app.change_model/perms.%s.change_%s/g' %s/templates/admin/%s/%s/%s_detail.html" % \
            (env.app_name, env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("rm %s/templates/admin/%s/%s/%s_detail.html.bak" % \
            (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        if not exists("%s/templates/admin/%s/%s/%s_confirm_delete.html" % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower())):
            local('curl https://gist.githubusercontent.com/guillaumepiot/b264c44696663678dc89/raw/model_confirm_delete.html > %s/templates/admin/%s/%s/%s_confirm_delete.html' \
                % (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Models\"/trans \"%s\"/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Model\"/trans \"%s\"/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/trans \"Delete model\"/trans \"Delete %s\"/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/Delete Model/Delete %s/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-add/%s-add/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-update/%s-update/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-detail/%s-detail/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-list/%s-list/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
        local("sed -i .bak 's/model-delete/%s-delete/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/model-admin/%s-admin/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.app_name, env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("sed -i .bak 's/following model/following %s/g' %s/templates/admin/%s/%s/%s_confirm_delete.html" % \
            (env.module_name.lower(), env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))

        local("rm %s/templates/admin/%s/%s/%s_confirm_delete.html.bak" % \
            (env.app_name, env.app_name, env.module_name.lower(), env.module_name.lower()))
