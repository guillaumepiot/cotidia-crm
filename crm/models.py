from django.db import models

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
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=2, choices=crm_settings.COUNTRIES, blank=True)

    # Website
    website = models.URLField(max_length=150, blank=True)

    date_created = models.DateTimeField(auto_now_add=True) 
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def title_verbal(self):
        return dict(crm_settings.TITLE).get(self.title)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)