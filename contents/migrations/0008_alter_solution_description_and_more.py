# Generated by Django 4.1.2 on 2022-12-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0007_alter_staff_github"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solution",
            name="description",
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="solutioncategory",
            name="description",
            field=models.TextField(max_length=10000),
        ),
    ]
