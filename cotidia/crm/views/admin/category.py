from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from cotidia.account.utils import StaffPermissionRequiredMixin
from cotidia.crm.models import Category
from cotidia.crm.forms.admin.category import (
    CategoryAddForm,
    CategoryUpdateForm)


class CategoryList(StaffPermissionRequiredMixin, ListView):
    model = Category
    template_name = 'admin/crm/category/category_list.html'
    permission_required = 'crm.change_category'

    def get_queryset(self):
        return Category.objects.filter()


class CategoryDetail(StaffPermissionRequiredMixin, DetailView):
    model = Category
    template_name = 'admin/crm/category/category_detail.html'
    permission_required = 'crm.change_category'


class CategoryCreate(StaffPermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'admin/crm/category/category_form.html'
    permission_required = 'crm.add_category'

    def get_success_url(self):
        messages.success(self.request, 'Category has been created.')
        return reverse(
            'crm-admin:category-detail',
            kwargs={'pk': self.object.id})


class CategoryUpdate(StaffPermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'admin/crm/category/category_form.html'
    permission_required = 'crm.change_category'

    def get_success_url(self):
        messages.success(self.request, 'Category details have been updated.')
        return reverse(
            'crm-admin:category-detail',
            kwargs={'pk': self.object.id}
            )


class CategoryDelete(StaffPermissionRequiredMixin, DeleteView):
    model = Category
    permission_required = 'crm.delete_category'
    template_name = 'admin/crm/category/category_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Category has been deleted.'))
        return reverse('crm-admin:category-list')
