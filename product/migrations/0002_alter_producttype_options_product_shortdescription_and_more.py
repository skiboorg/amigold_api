# Generated by Django 4.2.4 on 2023-08-13 07:20

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'Тип товара', 'verbose_name_plural': 'Типы товара'},
        ),
        migrations.AddField(
            model_name='product',
            name='shortDescription',
            field=models.TextField(blank=True, null=True, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='delivery',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Доставка и оплата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='product',
            name='feedingRate',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Норма кормления  '),
        ),
        migrations.AlterField(
            model_name='product',
            name='isPromotionActive',
            field=models.BooleanField(default=True, verbose_name='Отображать акционный блок?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotionText',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст в акционном блоке'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendorCode',
            field=models.CharField(max_length=255, null=True, verbose_name='Артикул'),
        ),
    ]