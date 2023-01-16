from django.contrib import admin
from .models import Product, ProductPicture


@admin.register(ProductPicture)
class ProductPictureAdmin(admin.ModelAdmin):
    empty_value_display = ""
    list_display = ("detail_picture",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = ""
    list_display = (
        "name",
        "product_thumbnail",
        "price",
        "discount_price",
        "weight",
        "product_description",
    )
    list_editable = ("price",)
