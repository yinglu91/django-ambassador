from administrator.views import AmbassadorAPIView
from rest_framework import serializers, exceptions
from rest_framework.permissions import IsAuthenticated
from common.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from core.models import Link, Product, Order,OrderItem, User
from .serializers import LinkSerializer, ProductSerializer, UserSerializer

from django.core.cache import cache
import time
import math
import random, string, decimal
from django_redis import get_redis_connection

class LinkAPIView(APIView):
  def get(self, _, code):
    link = Link.objects.filter(code=code).first()  # code is uniqe
    serializer = LinkSerializer(link)
    return Response(serializer.data)

    
class OrderAPIView(APIView):
  def post(self, request):
    data =  request.data
    link = Link.objects.filter(code=data['code']).first()

    if not link:
      raise exceptions.APIException('Invalid code!')

    order = Order()
    order.code = link.code
    order.user_id = link.user.id
    order.ambassador_email = link.user.email
    order.first_name = data['first_name']
    order.last_name = data['last_name']
    order.email = data['email']
    order.address = data['address']
    order.country = data['country']
    order.city = data['city']
    order.zip = data['zip']
    order.save()

    for item in data['products']:
        product = Product.objects.filter(pk=item['product_id']).first()
        quantity = decimal.Decimal(item['quantity'])

        order_item = OrderItem()
        order_item.order = order
        order_item.product_title = product.title
        order_item.price = product.price
        order_item.quantity = quantity
        order_item.ambassador_revenue = decimal.Decimal(.1) * product.price * quantity
        order_item.admin_revenue = decimal.Decimal(.9) * product.price * quantity
        order_item.save()


    return Response({
      'message': 'success'
    })