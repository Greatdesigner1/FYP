# Generated by Django 5.1.6 on 2025-04-13 14:19

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_alter_student_gender_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('100', '100L'), ('400', '400L'), ('300', '300L'), ('500', '500L'), ('200', '200L')], default='100', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='photos/'),
        ),
    ]
