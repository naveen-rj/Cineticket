from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView
from main.models import Movie, Cinema, Showtime, Booking, Seat


# Create your views here.

# View for listing movies
class MovieListView(ListView):
    model = Movie

    def get_queryset(self):
        queryset = super().get_queryset()
        cinema_name = self.request.GET.get('cinema')
        showtime_date = self.request.GET.get('showtime_date')

        # Filter movies based on showtimes at the specified cinema
        if cinema_name:
            queryset = queryset.filter(showtime__cinema__name__icontains=cinema_name).distinct()
        if showtime_date:
            queryset = queryset.filter(showtime__date=showtime_date)

        return queryset


# View for listing cinemas
class CinemaListView(ListView):
    model = Cinema

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


# View for search bar
class SearchListView(ListView):
    model = Movie

    def get_queryset(self):
        queryset = super().get_queryset()
        movie_name = self.request.GET.get('movie')

        # Get movie
        if movie_name:
            queryset = queryset.filter(title__icontains=movie_name)

        return queryset


# View for movies based on cinema
def cinema_movies(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    movies = cinema.movie_set.all()
    return render(request, 'movies_page.html', {'cinema': cinema, 'movies': movies})


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


# View for movie page
def movie(request, movie_id):
    mov = Movie.objects.get(pk=movie_id)

    # Filter Cinema objects based on the movie
    cinemas_showing_movie = Cinema.objects.filter(showtime__movie=mov).prefetch_related('showtime_set').distinct()

    context = {
        'movie': mov,
        'cinemas': cinemas_showing_movie
    }
    return render(request, 'movie.html', context)


@login_required
def seat_selection(request, showtime_id):
    if request.method == 'POST':
        selected_seat_ids = request.POST.getlist('selected_seats')

        # Store selected_seat_ids in the session
        request.session['selected_seat_ids'] = selected_seat_ids

        if not selected_seat_ids:
            messages.warning(request, 'No seat selected')
            url = reverse('seat', kwargs={'showtime_id': showtime_id})
            return redirect(url)

        # Get the number of tickets
        number_of_tickets = len(selected_seat_ids)

        if number_of_tickets > 5:
            messages.warning(request, 'Maximum 5 seats per booking!')
            url = reverse('seat', kwargs={'showtime_id': showtime_id})
            return redirect(url)

        selected_seats = Seat.objects.filter(id__in=selected_seat_ids)

        selected_seat_numbers = ', '.join([seat.number for seat in selected_seats])
        # Calculate the total price based on selected seats
        total_price = sum(seat.price for seat in selected_seats)

        # Get the showtime based on the showtime_id from the URL
        showtime = Showtime.objects.get(pk=showtime_id)
        total_amount = total_price + showtime.booking_fee

        context = {
            'ticket_count': number_of_tickets,
            'seats': selected_seat_numbers,
            'amount': total_price,
            'booking_fee': showtime.booking_fee,
            'total_amount': total_amount,
            'show': showtime,
        }

        return render(request, 'booking_summary.html', context)

    else:
        showtime = Showtime.objects.get(pk=showtime_id)
        seats = Seat.objects.filter(showtime=showtime)
        return render(request, 'seat_selection.html', {'showtime': showtime, 'seats': seats})


def confirm_booking(request, showtime_id):
    if request.method == 'POST':

        # Checking confirmation
        if request.POST.get('action') == 'confirm':

            # Accessing selected_seat_ids from the session
            if 'selected_seat_ids' in request.session:
                selected_seat_ids = request.session['selected_seat_ids']

                # Deleting selected_seat_ids from session
                del request.session['selected_seat_ids']

                selected_seats = Seat.objects.filter(id__in=selected_seat_ids)

                # Get the number of tickets
                number_of_tickets = len(selected_seat_ids)

                selected_seat_numbers = ', '.join([seat.number for seat in selected_seats])

                # Calculate the total price based on selected seats
                total_price = sum(seat.price for seat in selected_seats)

                # Get the showtime based on the showtime_id from the URL
                showtime = Showtime.objects.get(pk=showtime_id)
                total_amount = total_price + showtime.booking_fee

                # Create a booking record
                booking = Booking.objects.create(
                    user=request.user,
                    total_amount=total_amount,
                    showtime=showtime,
                    cinema=showtime.cinema,
                    movie=showtime.movie,
                    number_of_tickets=number_of_tickets,
                    seats=selected_seat_numbers,
                )

                # Mark selected seats as booked
                selected_seats.update(is_available=False)

                # Adding a success message
                messages.success(request, 'Hurray!!! Booking Confirmed!')

                return HttpResponseRedirect(reverse('ticket', kwargs={'booking_id': booking.id}))

            else:
                messages.info(request, 'You have already booked this seat!!!')
                return redirect(reverse('seat', kwargs={'showtime_id': showtime_id}))

        elif request.POST.get('action') == 'cancel':
            return redirect(reverse('seat', kwargs={'showtime_id': showtime_id}))

    return redirect('home')


def about(request):
    context = {
        'title': 'About Cineticket',
        'content': """
                Cineticket is a leading online movie ticket booking platform that offers a wide range of features and benefits to our customers. We offer the best prices on movie tickets, guaranteed. You can also save money by booking your tickets in advance or by taking advantage of our special offers. We offer a wide selection of movies to choose from, including the latest releases, blockbusters, and independent films. We also offer showtimes at a variety of theaters, so you can find the time and location that is most convenient for you.

                Booking tickets on Cineticket is easy and convenient. Just follow these simple steps:

                1. Visit our website and create an account.
                2. Select the movie you want to watch and the showtime you prefer.
                3. Select your preferred seats.
                4. Review your order and click "Confirm Booking".
                5. You will receive a confirmation e-ticket.

                On the day of the movie, simply show your confirmation e-ticket to the theater staff and they will scan your tickets. You can then enjoy the movie!

                We offer excellent customer support to our customers. If you have any questions or problems, please do not hesitate to contact us. We are here to help you make the most of your Cineticket experience.

                Thank you for choosing Cineticket! We hope to see you soon at the movies.
            """,
    }

    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html')
