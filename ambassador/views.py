from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from core.models import Product
from .serializers import ProductSerializer
from django.core.cache import cache
import time
import math


class ProductFrontendAPIView(APIView):
    @method_decorator(cache_page(60*60*2, key_prefix='products_frontend'))  # 2 hours
    def get(self, _):
      products = Product.objects.all()
      serializer = ProductSerializer(products, many=True)
      return Response(serializer.data)


class ProductBackendAPIView(APIView):

  def get(self, request):
    products = cache.get('products_backend')
    if not products:
      time.sleep(2) # 2 seconds for mimic the delay
      products = list(Product.objects.all())
      cache.set('products_backend', products, timeout=60*30)  # 30 minutes

    # search products
    s = request.query_params.get('s', '').lower()
    if s:
      products = list([
        p for p in products
        if (s in p.title.lower()) or (s in p.description.lower())
      ])

    total = len(products)

    # sort products
    sort = request.query_params.get('sort', None)
    if sort == 'asc':
      products.sort(key=lambda p: p.price)
    elif sort == 'desc':
      products.sort(key=lambda p: p.price, reverse=True)

    # paginate products
    per_page = 9
    page = int(request.query_params.get('page', 1))
    start = (page -1) * per_page
    end = page * per_page

    data = ProductSerializer(products[start:end], many=True).data
    return Response({
      'data': data,
      'meta': {
        'total': total,
        'page': page,
        'last_page': math.ceil(total / per_page)
      }
    })








    