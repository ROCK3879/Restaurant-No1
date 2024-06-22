from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make-booking/', views.make_booking, name='make_booking'),
    path('reservation-list/', views.reservation_list, name='reservation_list'),
    path('reservation-details/<int:booking_id>/', views.reservation_details, name='reservation_details'),
    path('cancel-reservation/<int:booking_id>/', views.cancel_reservation, name='cancel_reservation'),
]


