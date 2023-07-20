from rest_framework import generics

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Goods
from .serializers import GoodsSerializer

# Create your views here.


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "p"
    max_page_size = 100


# class GoodsListView(APIView):
#     """商品序列化"""

#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
class GoodsListView(generics.ListAPIView):
    """商品列表页"""

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
