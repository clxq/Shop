from django.db import models
from shop.models import Product


# Create your models here.
class Order(models.Model):
    name = models.CharField("用户名", max_length=50)
    tel = models.CharField("联系电话", max_length=11)
    address = models.CharField("地址", max_length=250)
    postal_code = models.CharField("邮政编码", max_length=20)
    created = models.DateTimeField("下单时间", auto_now_add=True)
    updated = models.DateTimeField("修改时间", auto_now_add=True)
    paid = models.BooleanField("支付状态", default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "订单编号{}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name="订单信息")
    product = models.ForeignKey(Product, related_name="order_items", verbose_name="商品信息")
    price = models.DecimalField("订单金额", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("商品数量", default=1)

    def __str__(self):
        return self.id

    def get_cost(self):
        return self.price * self.quantity
