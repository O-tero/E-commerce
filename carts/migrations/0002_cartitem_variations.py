# Generated by Django 4.2.7 on 2023-12-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_alter_variation_created_date_and_more"),
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="variations",
            field=models.ManyToManyField(blank=True, to="store.variation"),
        ),
    ]
