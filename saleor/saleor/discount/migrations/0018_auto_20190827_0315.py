# Generated by Django 2.2.4 on 2019-08-27 08:15

from django.db import migrations, models

from saleor.discount import VoucherType


def replace_removed_vocucher_type(apps, schema_editor):
    cls = apps.get_model("discount", "Voucher")
    cls.objects.filter(type="value").update(type=VoucherType.ENTIRE_ORDER)
    cls.objects.filter(type__in=["category", "product", "collection"]).update(
        type=VoucherType.SPECIFIC_PRODUCT
    )


class Migration(migrations.Migration):
    dependencies = [("discount", "0017_django_price_2")]

    operations = [
        migrations.RunPython(replace_removed_vocucher_type),
        migrations.AlterField(
            model_name="voucher",
            name="type",
            field=models.CharField(
                choices=[
                    ("entire_order", "Entire order"),
                    ("shipping", "Shipping"),
                    (
                        "specific_product",
                        "Specific products, collections and categories",
                    ),
                ],
                default="entire_order",
                max_length=20,
            ),
        ),
    ]