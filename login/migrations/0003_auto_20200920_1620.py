# Generated by Django 3.1 on 2020-09-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200920_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
