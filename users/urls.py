from django.urls import path
from .views import all_user_view

urlpatterns = [path("", all_user_view)]
