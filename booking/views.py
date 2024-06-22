from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking

def home(request):
    latest_bookings = Booking.objects.order_by('-date')[:5]
    return render(request, 'home.html', {'latest_bookings': latest_bookings})

@login_required
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('reservation_list')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

@login_required
def reservation_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'reservation_list.html', {'bookings': bookings})

@login_required
def reservation_details(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'reservation_details.html', {'booking': booking})

@login_required
def cancel_reservation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('reservation_list')
    return render(request, 'cancel_reservation.html', {'booking': booking})
