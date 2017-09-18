import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django_countries.fields import CountryField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def contacts(self):
        return Contact.objects.filter(category=self)\
            .order_by('company', 'first_name')

    class Meta:
        ordering = ['name']


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def contacts(self):
        return Contact.objects.filter(company=self).order_by('first_name')

    class Meta:
        ordering = ['name']


class Contact(models.Model):

    TITLE = (
        ('', '---'),
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('ms', 'Ms'),
        ('miss', 'Miss'),
        ('dr', 'Dr'),
        ('prof', 'Prof'),
        ('rev', 'Rev'),
        ('sir', 'Sir'),
    )

    title = models.CharField(
        max_length=10,
        choices=TITLE,
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
    country = CountryField(null=True)
    lat = models.DecimalField(
        max_digits=18, decimal_places=15, blank=True, null=True)
    lng = models.DecimalField(
        max_digits=18, decimal_places=15, blank=True, null=True)

    # Website
    website = models.URLField(max_length=150, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="user_created_contact"
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="user_modified_contact"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('first_name', 'last_name')

    def __str__(self):
        if self.title:
            return '{0} {1} {2}'.format(
                self.title_verbal, self.first_name, self.last_name)
        else:
            return '{0} {1}'.format(self.first_name, self.last_name)

    @property
    def title_verbal(self):
        return dict(self.TITLE).get(self.title)

    @property
    def country_verbal(self):
        return self.country

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
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="user_created"
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="user_modified"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.comment


class Action(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=3000, blank=True, null=True)
    due_date = models.DateField()
    due_time = models.TimeField(blank=True, null=True)
    completed = models.BooleanField(default=0)
    contact = models.ForeignKey('crm.Contact', blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="action_created"
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="action_modified"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return self.title

    def overdue(self):
        if self.completed:
            return False
        now = timezone.now()
        today = datetime.date(now.year, now.month, now.day)
        if today > self.due_date:
            return True
        return False


class Enquiry(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    data = models.TextField(null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return self.full_name
