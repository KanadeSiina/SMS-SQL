# Generated by Django 3.0.1 on 2019-12-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20191228_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='jbgz',
            field=models.IntegerField(),
        ),
    ]
