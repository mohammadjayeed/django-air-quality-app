from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="homepage" ),
    # path('app/',air_app,name="air-app"),
    
]
