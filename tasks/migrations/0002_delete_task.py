# Generated by Django 4.1.2 on 2022-10-25 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Task",
        ),
    ]
