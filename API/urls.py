from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from API import views

urlpatterns = [
  path(r'users/', views.get_users),
]