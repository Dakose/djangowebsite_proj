# Generated by Django 4.2.5 on 2023-11-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestnews', '0004_newsslider_news_image_alter_newsslider_news_css_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsslider',
            name='news_image',
            field=models.ImageField(null=True, upload_to='sliderimg/'),
        ),
    ]
