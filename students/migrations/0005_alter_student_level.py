# Generated by Django 5.1.6 on 2025-04-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('100', '100L'), ('200', '200L'), ('300', '300L'), ('400', '400L'), ('500', '500L')], default='100', max_length=20),
        ),
    ]
