import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

from crm import settings as crm_settings 

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return u'%s' % (self.name) 

    def contacts(self):
        return Contact.objects.filter(category=self)\
            .order_by('company', 'first_name')

    class Meta:
        ordering = [ 'name']
        verbose_name= 'Category'
        verbose_name_plural = 'Categories'

class Company(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return self.name

    def contacts(self):
        return Contact.objects.filter(company=self).order_by('first_name')

    class Meta:
        ordering = [ 'name']
        verbose_name= 'Company'
        verbose_name_plural= 'Companies'

class Contact(models.Model):

    title = models.CharField(
        max_length=10, 
        choices=crm_settings.TITLE, 
        blank=True, 
        null=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    company = models.ForeignKey(Company, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(
        upload_to='contact',
        max_length=100,
        blank=True,
        null=True)

    category = models.ManyToManyField('crm.Category', blank=True)

    # Phone
    phone_number = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=100, blank=True)

    # Email
    email = models.EmailField(max_length=100, blank=True)

    # Address
    first_line = models.CharField(max_length=100, blank=True)
    second_line = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=2, choices=crm_settings.COUNTRIES, blank=True)
    lat = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    lng = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)

    # Website
    website = models.URLField(max_length=150, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
        blank=True, null=True, related_name="user_created_contact")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
        blank=True, null=True, related_name="user_modified_contact")
    date_created = models.DateTimeField(auto_now_add=True) 
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('first_name', 'last_name')

    def __unicode__(self):
        if self.title:
            return u'%s %s %s' % (self.title_verbal, self.first_name, self.last_name)
        else:
            return u'%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        if self.title:
            return '%s %s %s' % (self.title_verbal, self.first_name, self.last_name)
        else:
            return u'%s %s' % (self.first_name, self.last_name)

    @property
    def title_verbal(self):
        return dict(crm_settings.TITLE).get(self.title)

    @property
    def country_verbal(self):
        return dict(crm_settings.COUNTRIES).get(self.country)

    @property
    def contact_number(self):
        if self.phone_number and self.mobile_number:
            return "%s / %s" % (self.phone_number, self.mobile_number)
        elif self.phone_number:
            return "%s" % (self.phone_number)
        elif self.mobile_number:
            return "%s" % (self.mobile_number)
        else:
            return ""

    def notes(self):
        return Note.objects.filter(contact=self)

    def actions(self):
        return Action.objects.filter(contact=self)

class Note(models.Model):
    comment = models.TextField(max_length=3000)
    contact = models.ForeignKey('crm.Contact', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
        blank=True, null=True, related_name="user_created")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
        blank=True, null=True, related_name="user_modified")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_created']

    def __unicode__(self):
        return u'%s' % (self.comment)

    def __str__(self):
        return '%s' % (self.comment)

class Action(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=3000, blank=True, null=True)
    due_date = models.DateField()
    due_time = models.TimeField(blank=True, null=True)
    completed = models.BooleanField(default=0)
    contact = models.ForeignKey('crm.Contact', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
        blank=True, null=True, related_name="action_created")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, \
        blank=True, null=True, related_name="action_modified")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-due_date']

    def __unicode__(self):
        return u'%s' % (self.title)

    def __str__(self):
        return '%s' % (self.title)

    def overdue(self):
        if self.completed:
            return False
        now = timezone.now()
        today = datetime.date(now.year, now.month, now.day)
        if today > self.due_date:
            return True
        return False