# Generated by Django 4.0.5 on 2022-06-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_repo', '0019_alter_image_owner_alter_image_time_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='time_uploaded',
            field=models.DateTimeField(default='2022-06-28 16:44:48', verbose_name='Upload Time'),
        ),
    ]
