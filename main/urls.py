from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.all_post),
    path('detail/<slug:slug>', views.detail),
    # path('', views.index),
]
