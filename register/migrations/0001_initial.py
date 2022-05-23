# Generated by Django 4.0.2 on 2022-03-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('Email', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Mobile', models.CharField(blank=True, default='', max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('DateModified', models.DateTimeField(auto_now=True)),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]