from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class TestimonialsSlider(models.Model):
    img = models.ImageField(upload_to='testimonialsimage/', validators=[FileExtensionValidator(['jpg', 'pdf', 'doc', 'svg'])])
    title = models.CharField(max_length=255, verbose_name='Testimonial title')
    text = models.CharField(max_length=255, verbose_name='Testimonial text')
    css = models.CharField(max_length=255, null=True, default='-', verbose_name='Testimonial css')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Testimonial slide'
        verbose_name_plural = 'Testimonial sliders'