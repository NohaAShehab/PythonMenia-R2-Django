# Generated by Django 4.1.7 on 2023-03-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/images'),
        ),
    ]
