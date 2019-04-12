# Generated by Django 2.2 on 2019-04-11 11:00

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id - primary key')),
                ('name', models.CharField(max_length=256, verbose_name='Название категории')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id - primary key')),
                ('availability', models.CharField(choices=[('NOT_AVAILABLE', 'Нет в наличии'), ('EXPECTED_DELIVERY', 'Ожидается поставка'), ('CAUSED', 'Вызывается'), ('IS_ENDING', 'Заканчивается'), ('IN_STOCK', 'В наличии'), ('IN_ARCHIVE', 'В архиве'), ('NOT_IN_STOCK', 'Нет на складе'), ('HIDDEN', 'Скрытый')], default='IN_STOCK', max_length=13, verbose_name='Доступность товара')),
                ('name', models.CharField(max_length=255, verbose_name='Имя продукта')),
                ('vendor_code', models.CharField(max_length=63, verbose_name='Артикул')),
                ('product_type', models.CharField(max_length=256, verbose_name='Вид товара')),
                ('brand', models.CharField(max_length=255, verbose_name='Бренд')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Наличие')),
                ('description', models.TextField(blank=True, max_length=4095, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена товара')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductImageURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка на картинку')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
    ]