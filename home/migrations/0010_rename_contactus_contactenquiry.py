# Generated by Django 4.0 on 2022-01-20 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_myblog_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactus',
            new_name='contactenquiry',
        ),
    ]