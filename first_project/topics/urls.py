from django.urls import path
from topics import views


urlpatterns = [
    path('', views.index,name='topics_index')
]
