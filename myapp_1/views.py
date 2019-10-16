from django.shortcuts import render
from rest_framework import generics
from .models import EmCategory,EmEmail,EmReceiver,EmGroup,EmUser,ScUser,GnGroupType
from .srializers import EmCategorySerializer,EmEmailSerializer,EmReceiverSerializer,EmGroupSerializer,EmUserSerializer,ScUserSerializer,GnGroupTypeSerializer




class EmCategoryAPIView(generics.ListCreateAPIView):
    queryset = EmCategory.objects.all()
    serializer_class = EmCategorySerializer

class EmEmailAPIView(generics.ListCreateAPIView):
    queryset = EmEmail.objects.all()
    serializer_class = EmEmailSerializer

class EmReceiverAPIView(generics.ListCreateAPIView):
    queryset = EmReceiver.objects.all()
    serializer_class = EmReceiverSerializer

class EmGroupAPIView(generics.ListCreateAPIView):
    queryset = EmGroup.objects.all()
    serializer_class = EmGroupSerializer

class EmUserAPIView(generics.ListCreateAPIView):
    queryset = EmUser.objects.all()
    serializer_class = EmUserSerializer

class ScUserAPIView(generics.ListCreateAPIView):
    queryset = ScUser.objects.all()
    serializer_class = ScUserSerializer

class GnGroupTypeAPIView(generics.ListCreateAPIView):
    queryset = GnGroupType.objects.all()
    serializer_class = GnGroupTypeSerializer
