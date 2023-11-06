# Generated by Django 4.2.5 on 2023-10-18 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StatusName', models.CharField(max_length=200, verbose_name='Status name')),
            ],
            options={
                'verbose_name': 'Status:',
                'verbose_name_plural': 'Status:',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateTimeField(auto_now=True)),
                ('order_name', models.CharField(max_length=200, verbose_name='Name:')),
                ('order_phone', models.CharField(max_length=200, verbose_name='Phone:')),
                ('order_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.statuscrm', verbose_name='Status:')),
            ],
            options={
                'verbose_name': 'Order:',
                'verbose_name_plural': 'Orders:',
            },
        ),
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Comment text')),
                ('comment_dt', models.DateTimeField(auto_now=True, verbose_name='Datatime making')),
                ('comment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Request')),
            ],
            options={
                'verbose_name': 'Comment:',
                'verbose_name_plural': 'Comments:',
            },
        ),
    ]
