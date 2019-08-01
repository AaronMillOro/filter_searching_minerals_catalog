from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mineral_search/', views.mineral_search, name ='mineral_search'),
    path('<int:pk>/', views.mineral_details, name ='mineral_details'),

]
