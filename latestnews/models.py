from django.db import models

# Create your models here.
class NewsSlider(models.Model):
    img = models.ImageField(upload_to='newssliderimage/')
    title = models.CharField(max_length=255, verbose_name='News title')
    text = models.CharField(max_length=255, verbose_name='News text')
    css = models.CharField(max_length=255, null=True, default='-', verbose_name='News CSS')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News slide'
        verbose_name_plural = 'News slides'


