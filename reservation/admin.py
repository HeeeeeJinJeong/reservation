from django.contrib import admin

# Register your models here.
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'people', 'start_date', 'end_date']
    search_fields = ['p_name']
    ordering = ['-updated_datetime', '-created']


admin.site.register(Reservation, ReservationAdmin)