from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.login, name='login'),
  path('signup/', views.signup, name='signup'),
  path('profile/<int:pk>', views.profile, name='profile'),
  path('logout/', views.logout, name='logout'),
]