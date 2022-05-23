# Generated by Django 4.0.2 on 2022-03-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_user_email_alter_user_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HOST',
            fields=[
                ('Email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Mobile', models.CharField(blank=True, default='', max_length=10)),
                ('Password', models.CharField(max_length=50)),
                ('DateModified', models.DateTimeField(auto_now=True)),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
