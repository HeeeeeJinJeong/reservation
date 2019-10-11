from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Reservation(models.Model):
    COMPLETE = 0
    WAITING = 1
    STATUS = (
        (COMPLETE, _("Complete")),
        (WAITING, _("Waiting")),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    p_name = models.CharField(max_length=30, blank=True, null=True)
    people = models.IntegerField(default=2)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    status = models.SmallIntegerField(choices=STATUS, default=WAITING)
    created = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=30)

    def get_absolute_url(self):
        # detail/<int:pk>/
        return reverse('reservation:detail', args=[self.id])

    def __str__(self):
        return str(self.p_name)