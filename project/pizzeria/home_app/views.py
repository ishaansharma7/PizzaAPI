from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from home_app.models import CreatedPizzas, Toppings, PizzaSize

# Create your views here.
def home(request):
    return render(request, 'home.html')

def created_pizza_list(request):
    access_pz_list = CreatedPizzas.objects.all()
    size_list = PizzaSize.objects.all()
    access_pz_dict = {'access_pz_list':access_pz_list, 'size_list':size_list}
    if request.method == 'POST':
        pizza_type = request.POST.get('pizza_type')
        pizza_size = request.POST.get('pizza_size')
        if pizza_type == 'All' and pizza_size == 'All':
           access_pz_list2 = CreatedPizzas.objects.all()
        elif pizza_type == 'All' and pizza_size != 'All':
            size_obj = PizzaSize.objects.get(pizza_size=pizza_size)
            access_pz_list2 = CreatedPizzas.objects.filter(pizza_size=size_obj)
        elif pizza_type != 'All' and pizza_size == 'All':
            access_pz_list2 = CreatedPizzas.objects.filter(pizza_type=pizza_type)
        else:
            size_obj = PizzaSize.objects.get(pizza_size=pizza_size)
            access_pz_list2 = CreatedPizzas.objects.filter(pizza_type=pizza_type, pizza_size=size_obj)
        access_pz_dict2 = {'access_pz_list':access_pz_list2, 'size_list':size_list}
        return render(request, 'created_pizza_list.html', access_pz_dict2)
    return render(request, 'created_pizza_list.html', access_pz_dict)

def create_pizza(request):
    size_list = PizzaSize.objects.all()
    toppings_list = Toppings.objects.all()
    context_dict = {'toppings_list':toppings_list, 'size_list':size_list}
    if request.method == 'POST':
        creator = request.POST.get('name')
        pizza_type = request.POST.get('pizza_type')
        pizza_size = request.POST.get('pizza_size')
        size_obj = PizzaSize.objects.get(pizza_size=pizza_size)
        pizza_topp_str = ''
        for topping in toppings_list:
            code = str(request.POST.get(f'{topping}'))
            if code != 'None':
                pizza_topp_str += code + ', '
        if pizza_topp_str == '':
            context_dict['alert_topp_emty'] = 1
            return render(request, 'create_pizza.html', context_dict)
        pizza_obj = CreatedPizzas(creator=creator, pizza_type=pizza_type, pizza_size=size_obj, pizza_toppings=pizza_topp_str)
        pizza_obj.save()
        context_dict['alert'] = 1
        return render(request, 'create_pizza.html', context_dict)
    return render(request, 'create_pizza.html', context_dict)

def edit_pizza(request, pk):
    size_list = PizzaSize.objects.all()
    toppings_list = Toppings.objects.all()

    selected_pizza = CreatedPizzas.objects.get(id=pk)

    context_dict = {'toppings_list':toppings_list, 'size_list':size_list, 'pk':pk, 'creator': selected_pizza.creator}

    if request.method == 'POST':
        creator = request.POST.get('name')
        pizza_type = request.POST.get('pizza_type')
        pizza_size = request.POST.get('pizza_size')
        size_obj = PizzaSize.objects.get(pizza_size=pizza_size)
        pizza_topp_str = ''
        for topping in toppings_list:
            code = str(request.POST.get(f'{topping}'))
            if code != 'None':
                pizza_topp_str += code + ', '
        if pizza_topp_str == '':
            context_dict['alert_topp_emty'] = 1
            return render(request, 'edit_pizza.html', context_dict)
        selected_pizza.creator = creator
        selected_pizza.pizza_type = pizza_type
        selected_pizza.pizza_size = size_obj
        selected_pizza.pizza_toppings = pizza_topp_str
        selected_pizza.save()
        context_dict['alert'] = 1
        return render(request, 'edit_pizza.html', context_dict)
    return render(request, 'edit_pizza.html', context_dict)

def add_variety(request):
    pizza_size = PizzaSize.objects.all()
    pizza_toppings = Toppings.objects.all()
    if request.method == 'POST':
        pizza_size_reci = request.POST.get('pizza_size')
        pizza_toppings_reci = request.POST.get('pizza_toppings')
        print(pizza_size_reci)
        print(len(pizza_toppings_reci))
        if len(pizza_size_reci) != 0:
            obj1 = PizzaSize(pizza_size=pizza_size_reci)
            obj1.save()
        if len(pizza_toppings_reci) != 0:
            obj2 = Toppings(pizza_toppings=pizza_toppings_reci)
            obj2.save()
        return render(request, 'addvariety.html', {'pizza_size': pizza_size, 'pizza_toppings':pizza_toppings})
    return render(request, 'addvariety.html', {'pizza_size': pizza_size, 'pizza_toppings':pizza_toppings})

def delete_pizza(request, pk):
    access_pz_list = CreatedPizzas.objects.all()
    access_pz_dict = {'access_pz_list':access_pz_list}
    if request.method == 'POST':
        CreatedPizzas.objects.get(pk=pk).delete()
        return render(request, 'created_pizza_list.html', access_pz_dict)
    return render(request, 'created_pizza_list.html', access_pz_dict)

def delete_size(request, pk):
    pizza_size = PizzaSize.objects.all()
    pizza_toppings = Toppings.objects.all()
    print('reached1')
    PizzaSize.objects.get(pk=pk).delete()
    return render(request, 'addvariety.html', {'pizza_size': pizza_size, 'pizza_toppings':pizza_toppings})
    # return render(request, 'addvariety.html', {'pizza_size': pizza_size, 'pizza_toppings':pizza_toppings})

def delete_toppings(request, pk):
    pizza_size = PizzaSize.objects.all()
    pizza_toppings = Toppings.objects.all()
    Toppings.objects.get(pk=pk).delete()
    return render(request, 'addvariety.html', {'pizza_size': pizza_size, 'pizza_toppings':pizza_toppings})
    # return render(request, 'addvariety.html', {'pizza_size': pizza_size, 'pizza_toppings':pizza_toppings})
