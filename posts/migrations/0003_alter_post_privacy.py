# Generated by Django 4.1.7 on 2023-02-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_created_at_post_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='privacy',
            field=models.CharField(choices=[('1', 'Public'), ('2', 'Private')], max_length=2),
        ),
    ]
