# Generated by Django 5.1.6 on 2025-02-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloge', '0003_post_created_at_alter_post_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(null=True),
        ),
    ]
