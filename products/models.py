from django.db import models
from django.core.validators import MinValueValidator


class ProductPicture(models.Model):
    detail_picture = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "ภาพรายละเอียดสินค้า"
        verbose_name_plural = "ภาพรายละเอียดสินค้า"
        db_table = "pictures"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="ชื่อผลิตภัณฑ์")
    price = models.PositiveSmallIntegerField(
        verbose_name="ราคา", validators=[MinValueValidator(1)]
    )
    discount_price = models.PositiveSmallIntegerField(
        verbose_name="ลดราคา", null=True, blank=True
    )
    product_thumbnail = models.URLField(verbose_name="ภาพขนาดย่อของผลิตภัณฑ์")
    product_pictures = models.ForeignKey(
        ProductPicture,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="ภาพรายละเอียดสินค้า",
    )
    product_description = models.TextField(
        verbose_name="คำอธิบายผลิตภัณฑ์", null=True, blank=True
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name="น้ำหนัก", validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "สินค้า"
        verbose_name_plural = "สินค้า"
        db_table = "products"
