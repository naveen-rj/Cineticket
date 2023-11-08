from django.urls import path

from main.views import MovieListView, home, movie, CinemaListView, cinema_movies, seat_selection, confirm_booking, \
    SearchListView, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('cinemas/', CinemaListView.as_view(), name='cinema_list'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('search/', SearchListView.as_view(), name='search'),
    path('cinemas/<int:cinema_id>/movies/', cinema_movies, name='cinema_movies'),  # Get movies based on cinema
    path('movies/<int:movie_id>', movie, name='movie'),  # movie page
    path('seat_selection/<int:showtime_id>', seat_selection, name='seat'),
    path('confirm_booking/<int:showtime_id>', confirm_booking, name='confirm_booking'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]