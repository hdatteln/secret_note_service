from django.urls import path
from apps.core.api import views as api_views

urlpatterns = [
    path('create_message', api_views.create_message, name='create-message')
]