from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('users', views.index),

]
