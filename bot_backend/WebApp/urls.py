from django.urls import path
from .views import *


urlpatterns = [
	path("code/<int:pk>/",Code_View,name='code'),	
]
