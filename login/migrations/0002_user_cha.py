# Generated by Django 3.0.1 on 2019-12-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cha',
            field=models.CharField(choices=[('student', '学生'), ('teacher', '教师')], default='学生', max_length=32),
        ),
    ]