# Generated by Django 4.1.2 on 2022-12-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0005_solution_solution_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="whitepaper",
            name="doi",
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="whitepaper",
            name="title",
            field=models.CharField(default="Tittle goes here", max_length=1000),
        ),
    ]
