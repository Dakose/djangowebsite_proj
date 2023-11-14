from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import NewsSlider

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_text', 'news_css')
    list_display_links = ('news_title', )
    list_editable = ('news_css', )
    fields = ('news_title', 'news_text', 'news_css')


admin.site.register(NewsSlider, NewsAdmin)