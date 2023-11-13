from django.db import models

# Create your models here.
class NewsSlider(models.Model):
    # news_img = models.CharField(upload_to='newsimg/')
    news_title = models.CharField(max_length=200, verbose_name='Title name')
    news_text = models.CharField(max_length=200, verbose_name='News text')
    news_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS class')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News slide'
        verbose_name_plural = 'News slides'


