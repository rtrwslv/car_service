from django.contrib import admin
from .models import Owner, Car, Repair, Maintenance, Appointment, Booking, Client

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Repair)
admin.site.register(Maintenance)
admin.site.register(Appointment)
admin.site.register(Booking)
admin.site.register(Client)
