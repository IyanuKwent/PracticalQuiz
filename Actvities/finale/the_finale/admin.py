from django.contrib import admin
from .models import Vehicle, Booking, Review, LoyaltyProgram, Location


admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(LoyaltyProgram)
admin.site.register(Location)