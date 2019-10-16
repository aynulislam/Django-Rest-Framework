from django.urls import path
from . views import EmCategoryAPIView,EmEmailAPIView,EmReceiverAPIView,EmGroupAPIView,EmUserAPIView,ScUserAPIView,GnGroupTypeAPIView

urlpatterns = [
	path('EmCategory/', EmCategoryAPIView, name="EmCategoryAPIView"),
    path('EmEmail/', EmEmailAPIView, name="EmEmailAPIView"),
	path('EmReceiver/', EmReceiverAPIView, name="EmReceiverAPIView"),
	path('EmGroup/', EmGroupAPIView, name="EmGroupAPIView"),
	path('EmUser/', EmUserAPIView, name="EmUserAPIView"),
	path('ScUser/', ScUserAPIView, name="ScUserAPIView"),
	path('GnGroup/', GnGroupTypeAPIView, name="GnGroupTypeAPIView"),







]
