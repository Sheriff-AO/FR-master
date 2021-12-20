from django.urls import path
from .import views


urlpatterns = [
    path('create_request_form', views.newRequestFormView, name='request_form')
]


# ---------------------------register this urls in the root urls------------------------------------------