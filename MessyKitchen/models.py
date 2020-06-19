from django.db import models
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
spice_choices=(
        ("low","low"),
        ("medium","medium"),
        ("high","high"),
    )
class Order(models.Model):
    First_Name = models.TextField(max_length=30)
    Last_Name = models.TextField(max_length=30)
    Email =models.EmailField()
    Phone_Number =PhoneNumberField()
    Your_Order = models.TextField()
    Spice_Choice=models.CharField(max_length=6, choices=spice_choices,default="low")