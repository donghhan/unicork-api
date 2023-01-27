from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserView.as_view(), name="view_and_create_user"),
    path(
        "<int:pk>",
        views.UserDetailView.as_view(),
        name="single_view_update_delete_user",
    ),
]
