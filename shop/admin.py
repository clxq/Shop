from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.site_header = "商城管理"

# 使用register装饰器注册
""" 
list_display:   指定要显示的字段
search_fields:   指定搜索的字段
list_filter:     指定列表过滤器
ordering：       指定排序字段
"""


@admin.register(Category)  # 单给某个表加一个定制
class CategoryAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ('name', 'slug')
    # slug关联字段设置
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'active', 'created', 'updated', 'isDelete')
    # 过滤器
    list_filter = ('active', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
