# Generated by Django 2.1.7 on 2020-04-28 07:31

import DjangoUeditor.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20200428_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='关于我们')),
            ],
            options={
                'verbose_name': '轮播图片',
                'verbose_name_plural': '轮播图片',
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='upimages/thumbnail/default.jpg', upload_to='upimages/news/', verbose_name='缩略图'),
        ),
        migrations.AlterField(
            model_name='newstype',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='upimages/products/default(2).jpg', upload_to='upimages/news/', verbose_name='缩略图'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='upimages/thumbnail/default.jpg', upload_to='upimages/products/', verbose_name='缩略图'),
        ),
    ]
