from django.urls import path
from first_app import views

#Template Tagging
app_name = 'first_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/', views.other,name='other'),
    path('table_access_records/',views.table_access_records,name='table_access_records'),
    path('home/',views.home,name='home'),
    path('form_name/',views.form_name_view,name='form_name'),
    path('store_details/',views.store_details,name='store_details'),
    path('signup/',views.signup,name='signup')
]
