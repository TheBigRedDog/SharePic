# Generated by Django 4.0.4 on 2022-05-20 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_repo', '0009_alter_image_time_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='time_uploaded',
            field=models.DateTimeField(default='2022-05-20 01:38:03', verbose_name='upload_time'),
        ),
    ]
