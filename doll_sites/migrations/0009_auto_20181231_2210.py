# Generated by Django 2.1.3 on 2018-12-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doll_sites', '0008_auto_20181231_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='model_name',
        ),
        migrations.AddField(
            model_name='photo',
            name='model_name',
            field=models.ManyToManyField(to='doll_sites.Actress'),
        ),
    ]
