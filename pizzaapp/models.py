from django.db import models
from email.policy import default
from django import forms
# Create your models here.

class Pizza(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    CRUST_CHOICES = [
        ('normal', 'Normal'),
        ('thin', 'Thin'),
        ('thick', 'Thick'),
        ('gluten_free', 'Gluten Free'),
    ]

    SAUCE_CHOICES = [
        ('tomato', 'Tomato'),
        ('bbq', 'BBQ'),
    ]

    CHEESE_CHOICES = [
        ('mozzarella', 'Mozzarella'),
        ('vegan', 'Vegan'),
        ('low_fat', 'Low Fat'),
    ]

    TOPPING_CHOICES = [
        ('pepperoni', 'Pepperoni'),
        ('chicken', 'Chicken'),
        ('ham', 'Ham'),
        ('pineapple', 'Pineapple'),
        ('peppers', 'Peppers'),
        ('mushrooms', 'Mushrooms'),
        ('onions', 'Onions'),
    ]

    size = models.CharField(max_length=10, choices=SIZE_CHOICES, null=True)
    crust = models.CharField(max_length=20, choices=CRUST_CHOICES, null=True)
    sauce = models.CharField(max_length=10, choices=SAUCE_CHOICES, null=True)
    cheese = models.CharField(max_length=10, choices=CHEESE_CHOICES, null=True)
    toppings = models.CharField(max_length=10, choices=TOPPING_CHOICES, null=True)

    def __str__(self):
        return f"{self.size} Pizza"

class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PizzaSize(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
