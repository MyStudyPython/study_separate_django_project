# Generated by Django 4.2.3 on 2023-07-18 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0002_alter_goods_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goodscategorybrand",
            name="add_time",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="添加时间"
            ),
        ),
    ]