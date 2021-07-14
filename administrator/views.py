from rest_framework import exceptions, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import User
from common.serializers import UserSerializer
from common.authentication import JWTAuthentication


class AmbassadorAPIView(APIView):
    def get(self, _):
      ambassadors = User.objects.filter(is_ambassador=True)
      serializer = UserSerializer(ambassadors, many=True)
      return Response(serializer.data)


