from django.contrib import admin
from main.models import Cinema, Movie, Showtime, Booking, Seat

# Register your models here.
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Booking)
admin.site.register(Seat)
