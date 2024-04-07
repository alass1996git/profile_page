from django.db import models

# Create your models here.

class bookingModel(models.Model):
    ID1 = models.IntegerField(max_length=5)
    Name = models.TextField(max_length=255)
    no_guests = models.IntegerField(max_length=6)
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name

class menuModel(models.Model):
    ID2 = models.IntegerField(max_length=11)
    Title = models.TextField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory=models.IntegerField(max_length=5)


    def __str__(self):
        return self.Title
