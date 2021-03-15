from django.urls import path
from auth_user_app import views

app_name = 'auth_user_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='login')
]
