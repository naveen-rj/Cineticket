from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from accounts.models import UserProfile
from main.models import Booking


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user registration

            # Create a UserProfile instance linked to the user
            UserProfile.objects.create(
                user=user,
                mobile_number=form.cleaned_data['mobile_number']
            )

            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to home page
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Username or Password'
    else:
        error_message = None
    return render(request, 'accounts/login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('home')


# Users profile
def profile(request):
    if request.method == 'POST':
        user = request.user  # Get the user
        user_profile = user.userprofile  # Get the user's profile

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        # Checking password
        if new_password1:
            form = PasswordChangeForm(user, data={'old_password': old_password, 'new_password1': new_password1,
                                                  'new_password2': new_password2})
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password Changed Successfully!')
            else:
                for error in form.errors.values():
                    messages.warning(request, error.as_text())
                return redirect('profile')

        user.save()  # Save the updated user fields

        user_profile.mobile_number = request.POST['mobile_number']

        # Handle profile pic upload
        if 'profile_pic' in request.FILES:
            user_profile.profile_pic = request.FILES['profile_pic']

        user_profile.save()  # Save the updated user profile

        messages.success(request, 'Profile Updated Successfully!')
        return redirect('profile')

    return render(request, 'accounts/profile.html')


# View for fetching all booking data of user
def booking_history(request):

    bookings = Booking.objects.filter(user=request.user).order_by('-date')

    return render(request, 'accounts/bookings.html', {'bookings': bookings})


# View for ticket details
def view_ticket(request, booking_id):

    ticket = Booking.objects.get(id=booking_id)

    return render(request, 'accounts/ticket.html', {'ticket': ticket})
