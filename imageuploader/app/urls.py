from . import views
from django.urls import path
urlpatterns = [
  path('',views.signup),
  path('signin',views.signin), 
  path('home',views.home), 
] 
