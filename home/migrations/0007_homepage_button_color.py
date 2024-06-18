# Generated by Django 4.2.8 on 2023-12-07 15:18

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_sidebar_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='button_color',
            field=wagtail_color_panel.fields.ColorField(default='#000000', max_length=7),
        ),
    ]