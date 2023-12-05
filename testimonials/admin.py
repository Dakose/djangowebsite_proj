from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import TestimonialsSlider

# Register your models here.
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'css', 'get_image')
    list_display_links = ('title', )
    list_editable = ('css', )
    fields = ('title', 'text', 'css', 'img', 'get_image')
    readonly_fields = ('get_image', )
    
    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="80px" ')
        else:
            return 'None image'
        
    get_image.short_description = 'minimize'

admin.site.register(TestimonialsSlider, TestimonialsAdmin)
