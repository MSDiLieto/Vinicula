from django.urls import path

from .import views

app_name = 'vinicula'

urlpatterns = [
    path('', views.MessageView.as_view(), name='vinicula_index')
]