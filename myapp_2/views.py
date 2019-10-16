
from django.shortcuts import render
from rest_framework import generics
from .models import EsUser, User, ScUser, GnGroupType, ChGroup, ChMessage, ChReceiver, ChUserGroup, ChConversation

from .serializers2  import EsUserSerializer,UserSerializer,ScUserSerializer,GnGroupTypeSerializer,\
    ChGroupSerializer,ChMessageSerializer,ChReceiverSerializer,ChUserGroupSerializer,ChConversation,ChConversationSerializer





class EsUserAPIView(generics.ListCreateAPIView):
    queryset = EsUser.objects.all()
    serializer_class = EsUserSerializer

class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ScUserAPIView(generics.ListCreateAPIView):
    queryset = ScUser.objects.all()
    serializer_class = ScUserSerializer

class ChMessageAPIView(generics.ListCreateAPIView):
    queryset = ChMessage.objects.all()
    serializer_class = ChMessageSerializer

class ChReceiverAPIView(generics.ListCreateAPIView):
    queryset = ChReceiver.objects.all()
    serializer_class = ChReceiverSerializer

class ScUserAPIView(generics.ListCreateAPIView):
    queryset = ScUser.objects.all()
    serializer_class = ScUserSerializer

class ChGroupAPIView(generics.ListCreateAPIView):
    queryset = ChGroup.objects.all()
    serializer_class = ChGroupSerializer

class ChUserGroupAPIView(generics.ListCreateAPIView):
    queryset = ChUserGroup.objects.all()
    serializer_class = ChUserGroupSerializer

class GnGroupTypeAPIView(generics.ListCreateAPIView):
    queryset = GnGroupType.objects.all()
    serializer_class = GnGroupTypeSerializer


class ChConversationAPIView(generics.ListCreateAPIView):
    queryset = ChConversation.objects.all()
    serializer_class = ChConversationSerializer
