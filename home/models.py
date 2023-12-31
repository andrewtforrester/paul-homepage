from django.db import models
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    profile_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, blank=True, null=True, related_name='+'
    )

    sidebar_color = ColorField(default="#000000")
    button_color = ColorField(default="#000000")

    

    page_body = StreamField([
        ('section', blocks.StructBlock([
            ('section_title', blocks.CharBlock()),
            ('section_content', blocks.StreamBlock([
                ('heading', blocks.CharBlock(form_classname="title")),
                ('paragraph', blocks.RichTextBlock()),
                ('numbered_list', blocks.StreamBlock([
                    ('item', blocks.RichTextBlock()),
                ])),
                ('image', ImageChooserBlock()),
                ('video_embed', blocks.TextBlock()),
            ]),)
        ])),
    ], collapsed=True, use_json_field=True)


    style_panels = [
        FieldPanel('profile_image'),
        NativeColorPanel('sidebar_color'),
        NativeColorPanel('button_color'),
    ]

    content_panels = [
        FieldPanel('page_body'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Page Content"),
        ObjectList(style_panels, heading="Page Style"),
        ObjectList(Page.promote_panels, heading='SEO'),
    ])

    content_panels = Page.content_panels + [



        
        

    ]
