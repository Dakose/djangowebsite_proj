from django.db import models

# Create your models here.
class ServiceSlider(models.Model):
    img = models.ImageField(upload_to='ourserviceimage/')
    title = models.CharField(max_length=255, verbose_name='Service name')
    text = models.CharField(max_length=255, verbose_name='Service text')
    css = models.CharField(max_length=255, null=True, default='-', verbose_name='Service css')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Service slide'
        verbose_name_plural = 'Service slides'