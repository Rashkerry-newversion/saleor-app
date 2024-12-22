# Generated by Django 2.1.2 on 2018-10-10 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("product", "0072_auto_20180925_1048")]

    operations = [
        migrations.AddField(
            model_name="attribute",
            name="product_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="temp_product_attributes",
                to="product.ProductType",
            ),
        ),
        migrations.AddField(
            model_name="attribute",
            name="product_variant_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="temp_variant_attributes",
                to="product.ProductType",
            ),
        ),
        migrations.AlterField(
            model_name="attribute", name="name", field=models.CharField(max_length=50)
        ),
        migrations.AlterField(
            model_name="attribute", name="slug", field=models.SlugField()
        ),
    ]