from django.db import models
from django.urls import reverse


# Create your models here.

# 分类模型
class Category(models.Model):
    name = models.CharField('分类名称', max_length=200)
    slug = models.CharField('slug', max_length=200, unique=True)
    created = models.DateTimeField('创建日期', auto_now_add=True)
    updated = models.DateTimeField('修改日期', auto_now=True)
    isDelete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


# 产品模型
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='分类')
    name = models.CharField('产品名称', max_length=200)
    slug = models.SlugField('slug', max_length=200, unique=True)
    image = models.ImageField('产品图片', upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('产品描述', blank=True)
    # max_digits=10,保留10位数字，decimal_places=2，保留2位小数点
    price = models.DecimalField('产品价格', max_digits=10, decimal_places=2)
    stock = models.IntegerField('产品库存')
    active = models.BooleanField('是否激活', default=True)
    created = models.DateTimeField('创建日期', auto_now_add=True)
    updated = models.DateTimeField('修改日期', auto_now=True)
    isDelete = models.BooleanField('是否删除', default=False)

    # 显示名称
    def __str__(self):
        return self.name

    # 定义一个用于拼接url的方法
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])
