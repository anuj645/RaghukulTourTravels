from django.urls import path
from . import views

urlpatterns = [
    path('',              views.tour_list,   name='tour_list'),
    path('create/',       views.tour_create, name='tour_create'),
    path('<slug:slug>/',  views.tour_detail, name='tour_detail'),
    path('<slug:slug>/edit/',   views.tour_update, name='tour_update'),
    path('<slug:slug>/delete/', views.tour_delete, name='tour_delete'),
]