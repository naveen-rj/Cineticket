from django.core.management.base import BaseCommand
from main.models import Showtime, Seat


class Command(BaseCommand):
    help = 'Create seats for shows'

    def handle(self, *args, **options):

        all_shows = Showtime.objects.all()  # Fetch all shows

        # Get shows for which seats are already created
        shows_with_seats = Seat.objects.values_list('showtime', flat=True).distinct()

        # Filter shows that don't have seats
        new_shows = all_shows.exclude(pk__in=shows_with_seats)

        for show in new_shows:

            for row in ['A', 'B', 'C', 'D']:
                for number in range(1, 11):
                    seat_number = row + str(number)

                    seat = Seat(
                        number=row + str(number),
                        is_available=True,  # Set the initial availability
                        price=200,  # Set the seat price
                        showtime=show  # Link the seat to the show
                    )
                    seat.save()

        self.stdout.write(self.style.SUCCESS('Seats created successfully.'))
