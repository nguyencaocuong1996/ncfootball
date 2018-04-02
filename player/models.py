from django.db import models
from django.conf import settings
# Create your models here.


class Player(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    dob = models.DateField(null=False, blank=False)
