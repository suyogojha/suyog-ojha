# Generated by Django 4.0 on 2022-02-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_myskillsabout'),
    ]

    operations = [
        migrations.CreateModel(
            name='mypersonalinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Age', models.CharField(blank=True, max_length=255, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('Freelance', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.CharField(blank=True, max_length=255, null=True)),
                ('Phone', models.CharField(blank=True, max_length=255, null=True)),
                ('Email', models.CharField(blank=True, max_length=255, null=True)),
                ('Langauges', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
