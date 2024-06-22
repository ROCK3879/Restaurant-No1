"""
URL configuration for restaurant_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant_reservation.urls')),  # Including URLs from the restaurant_reservation app
]

from django.urls import path
from .views import home  # Correct import statement

urlpatterns = [
    path('', home, name='home'),  # Map root URL to 'home' view
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('reservation-list/', views.reservation_list, name='reservation_list'),
    path('reservation-details/<int:reservation_id>/', views.reservation_details, name='reservation_details'),
    path('cancel-reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
]
