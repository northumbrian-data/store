# Generated by Django 3.1.4 on 2021-06-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0004_auto_20210614_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='recovery_key',
            field=models.TextField(),
        ),
    ]