# Generated by Django 5.1.6 on 2025-04-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_level'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='session',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='period',
            field=models.CharField(choices=[('MORNING', 'Morning'), ('EVENING', 'Evening')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('200', '200L'), ('400', '400L'), ('100', '100L'), ('300', '300L'), ('500', '500L')], default='100', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together={('date', 'period')},
        ),
    ]
