from rest_framework import exceptions, serializers, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import User, Product
from common.serializers import UserSerializer
from .serializers import ProductSerializer
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

    def get(self, request, pk=None):
      if pk:
        return self.retrieve(request, pk)

      return self.list(request)
    
    def post(self, request):
      return self.create(request)

    def put(self, request, pk=None):
      return self.partial_update(request, pk)

    def delete(self, request, pk=None):
      return self.destroy(request, pk)

