from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='movies/images', null=True)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    runtime = models.CharField(max_length=100, default='2h 45min')
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    trailer = models.CharField(max_length=255, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    showtime = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    booking_fee = models.IntegerField(null=True)

    class Meta:
        ordering = ('cinema', 'showtime')

    def __str__(self):
        return '{} | {} | {}'.format(self.cinema, self.movie, self.showtime)


class Seat(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    number = models.CharField(max_length=5, null=True)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.showtime} | Seat {self.number} ({'Available' if self.is_available else 'Booked'})"


class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    total_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    seats = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} | {self.movie}'
