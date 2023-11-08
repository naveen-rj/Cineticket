from django.urls import path
from accounts.views import signup, login_view, logout_view, profile, booking_history, view_ticket

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('bookings/', booking_history, name='bookings'),
    path('ticket/<int:booking_id>/', view_ticket, name='ticket'),
]
