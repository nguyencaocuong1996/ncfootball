from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', obtain_auth_token),
    path('change-password/', ChangePasswordView.as_view()),
]
