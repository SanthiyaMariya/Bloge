# Generated by Django 5.1.6 on 2025-02-25 07:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloge', '0002_alter_post_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
