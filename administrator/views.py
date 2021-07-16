from rest_framework import exceptions, serializers, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache

from core.models import User, Product, Link, Order, OrderItem
from common.serializers import UserSerializer
from .serializers import ProductSerializer, LinkSerializer, OrderSerializer
from common.authentication import JWTAuthentication


class AmbassadorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _):
      ambassadors = User.objects.filter(is_ambassador=True)
      serializer = UserSerializer(ambassadors, many=True)
      return Response(serializer.data)


class ProductGenericAPIView(
  generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin,
  mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @staticmethod
    def clear_products_cache():
      cache.delete('products_backend')
      
      for key in cache.keys('*'):
        if 'products_frontend' in key:
          cache.delete(key)


    def get(self, request, pk=None):
      if pk:
        return self.retrieve(request, pk)

      return self.list(request)
    
    def post(self, request):
      resonse = self.create(request)
      self.clear_products_cache()
      return resonse

    def put(self, request, pk=None):
      resonse = self.partial_update(request, pk)
      self.clear_products_cache()
      return resonse

    def delete(self, request, pk=None):
      resonse = self.destroy(request, pk)
      self.clear_products_cache()
      return resonse


class LinkAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
      links = Link.objects.filter(user_id=pk)
      serializer = LinkSerializer(links, many=True)
      return Response(serializer.data)


class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
      orders = Order.objects.filter(complete=True)
      serializer = OrderSerializer(orders, many=True)
      return Response(serializer.data)

      