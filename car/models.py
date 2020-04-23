from django.db import models
from django.urls import reverse 

class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.IntegerField()

    is_available = models.BooleanField()

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Booking(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE) 
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone_number = models.PositiveIntegerField()
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    booking_message = models.TextField()
    is_approved = models.BooleanField()
