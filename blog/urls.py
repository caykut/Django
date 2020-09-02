from django.urls import path
from . import views
urlpatterns=[
    path('',views.homee,name='homee'),
    path('homepage',views.homepage,name='homepage'),
   
]