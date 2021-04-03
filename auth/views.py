from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import RegistrationSerializer


@api_view(['GET'])
def api_auth_root(request):
    return Response({
        'register': reverse('register', request=request),
        'token': reverse('token_obtain_pair', request=request),
        'token_refresh': reverse('token_refresh', request=request),
    })


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
