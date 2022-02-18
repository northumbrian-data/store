# Generated by Django 3.1.4 on 2022-02-02 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myauth", "0026_auto_20220125_1539"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plugin",
            name="teams",
        ),
        migrations.AddField(
            model_name="plugin",
            name="team",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to="myauth.team"),
        ),
    ]