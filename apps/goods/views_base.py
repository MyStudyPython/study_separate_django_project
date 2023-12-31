# 用于 JSON 数据的序列化与反序列化
import json

from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from goods.models import Goods


class MyEncoder(json.JSONEncoder):
    """
    自定义一个 JSON 编码器的子类，
    用于将 bytes 类型的数据转换为字符串类型
    """

    def default(self, obj):
        """
        重写默认的 default 方法，在遇到对象类型为 bytes 时进行特殊处理
        """
        if isinstance(obj, bytes):  # 判断对象是否属于 bytes 类型
            return str(obj, encoding="utf-8")

        # 如果对象不是 bytes 类型，则调用父类的 default 方法进行默认处理
        return json.JSONEncoder.default(self, obj)


# class GoodsListView(View):
#     "如果对象不是 bytes 类型，则调用父类的 default 方法进行默认处理"

#     def get(self, request):  # 定义 get 方法，处理 GET 请求
#         """通过View实现商品列表页"""
#         json_list = []
#         goods = Goods.objects.all()[:10]  # 查询商品模型中的前 10 条记录

#         """
#         使用Django自带的model_to_dict()方法可以实现直接将模型数据转化为字典形式，
#         但是对于DateTimeField、ImageField等字段时还是无法序列化，
#         因此需要使用serializer进行序列化
#         """
#         json_data = serializers.serialize("json", goods)
#         json_data = json.loads(json_data)
#         # for good in goods:
#         #     json_dict = {}
#         #     json_dict["name"] = good.name
#         #     json_dict["category"] = good.category.name
#         #     json_dict["market_price"] = good.market_price
#         # 如 datetime 不能直接用 json.dumps() 方法序列化
#         #     json_dict["add_time"] = good.add_time
#         #     json_list.append(json_dict)

#         """
#         将 JSON 列表进行序列化，并返回一个 JSON 响应，设置响应的 Content-Type 为 “application/json”

#         json.dumps(): 是一个 JSON 序列化方法，用于将 Python 对象转换为 JSON 字符串

#         ensure_ascii=False:
#         是 json.dumps() 方法的一个参数，用于指定是否将非 ASCII 字符转义为 Unicode 转义序列。
#         在上述代码中，设置为 False，表示不进行 ASCII 编码，保留非 ASCII 字符
#         """
#         # return HttpResponse(
#         #     json.dumps(json_list, ensure_ascii=False), content_type="application/json"
#         # )
#         return HttpResponse(json.dumps(json_list, ensure_ascii=False))


class GoodsListView(View):
    def get(self, request):
        """通过serializers实现商品列表页"""
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize("json", goods)
        return JsonResponse(json.loads(json_data), safe=False)
