# Generated by Django 4.2.8 on 2024-06-19 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_genericsitesettings_philpeople_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericsitesettings',
            name='philpeople_link',
            field=models.CharField(default='', max_length=1023),
            preserve_default=False,
        ),
    ]