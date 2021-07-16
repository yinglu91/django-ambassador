from administrator.views import AmbassadorAPIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from common.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from core.models import Link, Product, Order, User
from .serializers import LinkSerializer, ProductSerializer, UserSerializer

from django.core.cache import cache
import time
import math
import random, string
from django_redis import get_redis_connection

class LinkAPIView(APIView):
  def get(self, _, code):
    link = Link.objects.filter(code=code).first()  # code is uniqe
    serializer = LinkSerializer(link)
    return Response(serializer.data)

    
