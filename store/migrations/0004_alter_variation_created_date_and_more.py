# Generated by Django 4.2.7 on 2023-12-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_variation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variation",
            name="created_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="variation",
            name="variation_value",
            field=models.CharField(max_length=100),
        ),
    ]
