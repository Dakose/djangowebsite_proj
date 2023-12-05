# Generated by Django 4.2.5 on 2023-12-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='newssliderimage/')),
                ('title', models.CharField(max_length=255, verbose_name='News title')),
                ('text', models.CharField(max_length=255, verbose_name='News text')),
                ('css', models.CharField(default='-', max_length=255, null=True, verbose_name='News CSS')),
            ],
            options={
                'verbose_name': 'News slide',
                'verbose_name_plural': 'News slides',
            },
        ),
    ]
