from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.user)
