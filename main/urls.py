from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.all_post),
    path('detail/', views.detail),
    # path('', views.index),
]
