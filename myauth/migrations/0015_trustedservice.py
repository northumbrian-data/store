# Generated by Django 3.1.4 on 2021-08-24 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myauth", "0014_invite_is_collaborator"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrustedService",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("base_url", models.URLField()),
                ("team", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="myauth.team")),
            ],
        ),
    ]
