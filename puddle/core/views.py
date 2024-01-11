from django.shortcuts import render, redirect
from item.models import Category, Item
from . forms import SignUpForm
from django.contrib.auth import logout, authenticate


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {
        'form': form
    })


def logout_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    logout(request)

    return redirect('/login/')

