# Generated by Django 4.0 on 2022-02-06 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_delete_myprofilepic_myskillsabout_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myskillsabout',
            name='image',
        ),
    ]