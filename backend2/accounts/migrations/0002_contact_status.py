# Generated by Django 2.2.7 on 2019-11-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]