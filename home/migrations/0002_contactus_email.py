# Generated by Django 4.0 on 2022-01-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]