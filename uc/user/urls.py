from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='user_login'),
    path('sign_in/', views.Register.as_view(), name='user_register'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('home/', views.Index.as_view(), name='user_index'),
]
