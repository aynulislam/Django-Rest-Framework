from django.urls import path
from . views import  EsUserAPIView,UserAPIView,ScUserAPIView,GnGroupTypeAPIView, ChConversationAPIView,ChGroupAPIView,ChMessageAPIView,ChReceiverAPIView,ChUserGroupAPIView

urlpatterns = [
	path('EsUser/',  EsUserAPIView, name="EsUserAPIView"),
    path('User/', UserAPIView, name="UserAPIView"),
	path('ScUser/', ScUserAPIView, name="ScUserAPIView"),
	path('GnGroupType/', GnGroupTypeAPIView, name="GnGroupAPIView"),
	path('ChConversation/', ChConversationAPIView, name="ChConversationAPIView"),
	path('ChGroup/', ChGroupAPIView, name="ChGroupAPIView"),
	path('ChMessage/.', ChMessageAPIView, name="ChMessageAPIView"),
    path('ChReceiver/', ChReceiverAPIView, name="ChReceiverAPIView"),
    path('ChUserGroup/', ChUserGroupAPIView, name="ChUserGroupAPIView"),
]