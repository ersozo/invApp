# Generated by Django 5.0.4 on 2024-08-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("sku", models.CharField(max_length=50, unique=True)),
                ("price", models.FloatField()),
                ("quantity", models.IntegerField(default=0)),
                ("supplier", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "product",
            },
        ),
    ]
