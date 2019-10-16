"""project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myapp_1.views import ( EmUserAPIView, EmGroupAPIView,
                            EmCategoryAPIView, EmEmailAPIView,
                            EmReceiverAPIView, ScUserAPIView, GnGroupTypeAPIView)

from myapp_2.views import  ( EsUserAPIView, UserAPIView, ScUserAPIView, GnGroupTypeAPIView,
                            ChGroupAPIView, ChMessageAPIView, ChReceiverAPIView, ChUserGroupAPIView, ChConversationAPIView)




urlpatterns = [
    path('myapp_1', include('myapp_1.urls')),
    path('admin/', admin.site.urls),
    path('myapp_2/', include('myapp_2.urls')),


    path('EmCategory', EmCategoryAPIView.as_view(), name='EmCategory-list'),
    path('EmEmail', EmEmailAPIView.as_view(), name=' EmEmail-list'),
    path('EmReceiver', EmReceiverAPIView.as_view(), name='EmReceiver-list'),
    path('EmGroup', EmGroupAPIView.as_view(), name='EmGroup-list'),
    path('ScUser', ScUserAPIView.as_view(), name='ScUser-list'),
    path('GnGroupType', GnGroupTypeAPIView.as_view(), name='GnGroupType-list'),
    path('EmUserGroup', EmUserAPIView.as_view(), name='EmUserGroup-list'),


    path('EsUser', EsUserAPIView.as_view(), name='EsUser-list'),
    path('User', UserAPIView.as_view(), name=' User-list'),
    path('ScUser', ScUserAPIView.as_view(), name='ScUser-list'),
    path('GnGroupType', GnGroupTypeAPIView.as_view(), name='GnGroup-list'),
    path('ChGroup', ChGroupAPIView.as_view(), name='ChGroup-list'),
    path('ChMessage', ChMessageAPIView.as_view(), name='ChMessage-list'),
    path('ChReceiver', ChReceiverAPIView.as_view(), name='ChReciever-list'),
    path('ChUserGroup', ChUserGroupAPIView.as_view(), name='ChUserGroup-list'),
    path('ChConversation', ChConversationAPIView.as_view(), name='ChConversation-list')

]
