from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import NewsSlider

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_text', 'news_css', 'get_image')
    list_display_links = ('news_title', )
    list_editable = ('news_css', )
    fields = ('news_title', 'news_text', 'news_css', 'news_img', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        if obj.news_img:
            return mark_safe(f'<img src="{obj.news_img.url}" width="80px" ')
        else:
            return 'None image'

    get_image.short_description = 'minimize'

admin.site.register(NewsSlider, NewsAdmin)