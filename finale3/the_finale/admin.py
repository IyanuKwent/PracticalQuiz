from django.contrib import admin
from .models import Post, Comment, Vehicle, Booking, Location, Review, LoyaltyProgram

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Location)
admin.site.register(Review)
admin.site.register(LoyaltyProgram)
