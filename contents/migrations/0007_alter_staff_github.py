# Generated by Django 4.1.2 on 2022-12-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0006_whitepaper_doi_whitepaper_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="github",
            field=models.URLField(blank=True, max_length=999),
        ),
    ]