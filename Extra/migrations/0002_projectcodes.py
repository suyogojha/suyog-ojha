# Generated by Django 4.0 on 2022-02-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectcodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
