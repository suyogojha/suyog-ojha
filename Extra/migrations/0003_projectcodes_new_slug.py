# Generated by Django 4.0 on 2022-02-05 11:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0002_projectcodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcodes',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
