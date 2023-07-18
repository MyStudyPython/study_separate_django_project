# Generated by Django 4.2.3 on 2023-07-18 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_goodscategory_add_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brands', to='goods.goodscategory', verbose_name='商品类目'),
        ),
    ]