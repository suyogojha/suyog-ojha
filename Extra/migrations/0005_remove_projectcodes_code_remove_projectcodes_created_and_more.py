# Generated by Django 4.0 on 2022-02-05 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0004_alter_projectcodes_new_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcodes',
            name='code',
        ),
        migrations.RemoveField(
            model_name='projectcodes',
            name='created',
        ),
        migrations.RemoveField(
            model_name='projectcodes',
            name='modified',
        ),
    ]
