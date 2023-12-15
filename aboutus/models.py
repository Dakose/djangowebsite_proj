from django.db import models

# Create your models here.
class AboutUs(models.Model):
    img = models.ImageField(upload_to='aboutus/')
    title = models.CharField(max_length=255, verbose_name='title')
    text = models.CharField(max_length=255, verbose_name='text')
    css = models.CharField(max_length=255, null=True, default='-', verbose_name='about css')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural ='About us'