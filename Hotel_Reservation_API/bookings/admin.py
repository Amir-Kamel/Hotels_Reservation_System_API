from django.contrib import admin
from .models import *

admin.site.register(Booking)
admin.site.register(BookingCartItem)
admin.site.register(BookingCartSummary)