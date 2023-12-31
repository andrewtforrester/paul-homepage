# Generated by Django 4.2.8 on 2023-12-07 16:06

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_button_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='page_body',
            field=wagtail.fields.StreamField([('section', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock()), ('section_content', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video_embed', wagtail.blocks.TextBlock())]))]))], use_json_field=True),
        ),
    ]
