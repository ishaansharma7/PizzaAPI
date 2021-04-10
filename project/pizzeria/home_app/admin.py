from django.contrib import admin
from home_app.models import PizzaSize, Toppings, CreatedPizzas
# Register your models here.
admin.site.register(PizzaSize)
admin.site.register(Toppings)
admin.site.register(CreatedPizzas)