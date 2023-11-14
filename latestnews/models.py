from django.db import models

# Create your models here.
class NewsSlider(models.Model):
    news_title = models.CharField(max_length=100, verbose_name='Title name')
    news_text = models.CharField(max_length=255, verbose_name='News text')
    news_css = models.CharField(max_length=255, null=True, default='-', verbose_name='CSS class')

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'News slide'
        verbose_name_plural = 'News slides'


