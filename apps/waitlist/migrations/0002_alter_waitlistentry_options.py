# Generated by Django 3.2 on 2021-12-10 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waitlistentry',
            options={'verbose_name_plural': 'Waitlist entries'},
        ),
    ]