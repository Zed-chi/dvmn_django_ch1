# Generated by Django 3.1.3 on 2020-11-23 18:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20201120_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Детальное описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, default='', verbose_name='Короткое описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
    ]