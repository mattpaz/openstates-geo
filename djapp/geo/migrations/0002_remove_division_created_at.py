# Generated by Django 3.0.5 on 2020-04-15 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="division",
            name="created_at",
        ),
    ]
