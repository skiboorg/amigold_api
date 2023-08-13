# Generated by Django 4.2.4 on 2023-08-13 07:08

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('isPromotionActive', models.BooleanField(default=False, verbose_name='Отображать акционный блок?')),
                ('promotionText', models.CharField(blank=True, max_length=255, verbose_name='Текст в акционном блоке')),
                ('vendorCode', models.CharField(max_length=255, verbose_name='Артикул')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, help_text='Если не заполнено, создается на основе поля Назавание', max_length=255, null=True, verbose_name='ЧПУ')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Состав')),
                ('feedingRate', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Норма кормления  ')),
                ('delivery', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Доставка и оплата')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=3, default=0, max_digits=6, null=True, verbose_name='Вес, кг')),
                ('textLabel', models.CharField(max_length=20, null=True, verbose_name='Название')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Стоимость')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='product.product')),
            ],
            options={
                'verbose_name': 'Цена/Вес товара',
                'verbose_name_plural': 'Цены/Веса товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[720, 440], upload_to='product/gallery')),
                ('imageThumb', models.ImageField(blank=True, editable=False, null=True, upload_to='product/gallery/')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основная картинка')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='product.product')),
            ],
            options={
                'verbose_name': 'Картинка товара',
                'verbose_name_plural': 'Картинки товаров',
                'ordering': ('is_main',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.ManyToManyField(blank=True, to='product.producttype'),
        ),
    ]