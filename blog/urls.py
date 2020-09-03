from django.urls import path
from . import views
urlpatterns=[
    path('',views.homee,name='homee'),
    path('homepage',views.homepage,name='homepage'),
    path('register',views.register,name='register'),
    path('myview',views.my_view,name='myview'),
    path('home_page',views.home,name='home_page'),
    
    
  




    
    
 
]