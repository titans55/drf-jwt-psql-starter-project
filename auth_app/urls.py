from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = (
    # urls for Django Rest Framework API
    path('obtain-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
)
