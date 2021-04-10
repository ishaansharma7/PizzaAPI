from django.db import models

# Create your models here.
class PizzaSize(models.Model):
    pizza_size = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.pizza_size

class Toppings(models.Model):
    pizza_toppings = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.pizza_toppings

class CreatedPizzas(models.Model):
    creator = models.CharField(max_length=250)
    pizza_type = models.CharField(max_length=250)
    pizza_size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    pizza_toppings = models.CharField(max_length=500)

    def __str__(self):
        return self.creator