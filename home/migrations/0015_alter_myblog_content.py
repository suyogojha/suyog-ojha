# Generated by Django 4.0 on 2022-01-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_myblog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
