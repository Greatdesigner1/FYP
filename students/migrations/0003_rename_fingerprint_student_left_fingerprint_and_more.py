# Generated by Django 5.1.6 on 2025-04-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_attendance_day_remove_attendance_period_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fingerprint',
            new_name='left_fingerprint',
        ),
        migrations.AddField(
            model_name='student',
            name='right_fingerprint',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('300', '300L'), ('100', '100L'), ('500', '500L'), ('200', '200L'), ('400', '400L')], default='100', max_length=20),
        ),
    ]
