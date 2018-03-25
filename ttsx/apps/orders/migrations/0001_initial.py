# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(verbose_name='添加时间', auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.DecimalField(verbose_name='单价', max_digits=10, decimal_places=2)),
                ('comment', models.TextField(default='', verbose_name='评价信息')),
            ],
            options={
                'db_table': 'df_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('add_date', models.DateTimeField(verbose_name='添加时间', auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('order_id', models.CharField(serialize=False, verbose_name='订单号', max_length=64, primary_key=True)),
                ('total_count', models.IntegerField(default=1, verbose_name='商品总数')),
                ('total_amount', models.DecimalField(verbose_name='商品总金额', max_digits=10, decimal_places=2)),
                ('trans_cost', models.DecimalField(verbose_name='运费', max_digits=10, decimal_places=2)),
                ('pay_method', models.SmallIntegerField(default=1, verbose_name='支付方式', choices=[(1, '货到付款'), (2, '支付宝')])),
                ('status', models.SmallIntegerField(default=1, verbose_name='订单状态', choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')])),
                ('trade_id', models.CharField(verbose_name='支付编号', unique=True, blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'df_order_info',
            },
        ),
    ]
