# Generated by Django 4.2.5 on 2023-11-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestnews', '0005_alter_newsslider_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsslider',
            name='news_image',
            field=models.ImageField(upload_to='sliderimg/'),
        ),
    ]
