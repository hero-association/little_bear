# Generated by Django 2.1.3 on 2018-12-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doll_sites', '0006_photo_vip_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='download_link',
            field=models.CharField(blank=True, max_length=360, null=True),
        ),
    ]
