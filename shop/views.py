from django.shortcuts import render
from .models import Category, Product
from cart.forms import CatAddProductForm


# Create your views here.

# 产品列表信息
def product_list(request, category_slug=None):
    category = None
    # 获取所有的分类
    categorys = Category.objects.all()
    # 获取激活状态的产品
    products = Product.objects.all().filter(active=True)
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = category.products.all().filter(active=True)
        # products=products.filter(category=category) # 与上一行效果一样
    return render(request, 'shop/product/list.html', locals())


# 产品详情
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    cart_product_form = CatAddProductForm()
    return render(request, 'shop/product/detail.html', locals())
