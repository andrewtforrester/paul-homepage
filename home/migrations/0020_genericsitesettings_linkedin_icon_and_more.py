# Generated by Django 4.2.8 on 2024-06-19 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0019_genericsitesettings_philpeople_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericsitesettings',
            name='linkedin_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='genericsitesettings',
            name='linkedin_link',
            field=models.CharField(default='', max_length=1023),
            preserve_default=False,
        ),
    ]
