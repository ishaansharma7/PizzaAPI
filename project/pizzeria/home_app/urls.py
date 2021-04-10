from django.urls import path
from home_app import views

app_name = 'home_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('pizzalist/', views.created_pizza_list, name='created_pizza_list'),
    path('create/', views.create_pizza, name='create'),
    path('edit/<int:pk>', views.edit_pizza, name='edit'),
    path('addvariety/', views.add_variety, name='addvariety'),
    path('delete/<int:pk>', views.delete_pizza, name='delete'),
    path('delete_size/<int:pk>', views.delete_size, name='delete_size'),
    path('delete_toppings/<int:pk>', views.delete_toppings, name='delete_toppings'),
]