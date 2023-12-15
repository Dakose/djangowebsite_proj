# Generated by Django 4.2.5 on 2023-12-15 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='aboutus/')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
                ('css', models.CharField(default='-', max_length=255, null=True, verbose_name='about css')),
            ],
            options={
                'verbose_name': 'About us',
                'verbose_name_plural': 'About us',
            },
        ),
    ]