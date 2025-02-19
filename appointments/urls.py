from django.urls import path
from appointments import views

urlpatterns = [
    path('slots/', views.get_available_slots),
    path('appointments/', views.create_appointment),
]