# Generated by Django 2.0.2 on 2018-03-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20180314_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='enquiry_type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
