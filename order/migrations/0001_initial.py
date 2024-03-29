# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-26 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0003_auto_20181226_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('tel', models.CharField(max_length=11, verbose_name='联系电话')),
                ('address', models.CharField(max_length=250, verbose_name='地址')),
                ('post_code', models.CharField(max_length=20, verbose_name='邮政编码')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('paid', models.BooleanField(default=False, verbose_name='支付状态')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单金额')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='商品数量')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.Order', verbose_name='订单信息')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product', verbose_name='商品信息')),
            ],
        ),
    ]
