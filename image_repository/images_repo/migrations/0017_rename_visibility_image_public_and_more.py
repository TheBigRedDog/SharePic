# Generated by Django 4.0.4 on 2022-05-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_repo', '0016_alter_image_owner_alter_image_time_uploaded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='visibility',
            new_name='public',
        ),
        migrations.AlterField(
            model_name='image',
            name='time_uploaded',
            field=models.DateTimeField(default='2022-05-20 19:34:41', verbose_name='Upload Time'),
        ),
    ]
