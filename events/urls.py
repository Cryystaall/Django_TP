# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # La vue pour afficher la liste des événements
    path('<int:id_event>/', views.event_detail, name='event_detail'),  # La vue pour afficher le détail de l'événement
]
