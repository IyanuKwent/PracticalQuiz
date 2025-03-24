from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Vehicle(models.Model):
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    transmission = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'tbl_vehicle'
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return f"{self.model} ({self.type})"

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tbl_location'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)

    class Meta:
        db_table = 'tbl_booking'
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        
    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'tbl_review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return f"Review by {self.user.username} - {self.rating}/5"


class LoyaltyProgram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        db_table = 'tbl_loyalty'
        verbose_name = 'Loyalty'
        verbose_name_plural = 'Loyalties'
        
    def __str__(self):
        return f"{self.user.username} - {self.points} points"

class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
          return self.title

class Comment(models.Model):
        content = models.TextField()
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)