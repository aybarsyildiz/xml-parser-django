# Generated by Django 3.1.7 on 2021-10-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xmlmodel',
            name='email_of_user',
            field=models.TextField(null=True),
        ),
    ]
