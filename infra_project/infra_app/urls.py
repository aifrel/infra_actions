from django.urls import path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', views.index, name='/'),
    path('second/', views.second_page, name='second'),

]
