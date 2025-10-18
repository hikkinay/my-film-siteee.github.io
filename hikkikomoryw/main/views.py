from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm




def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') #перенаправление не страницу логин
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})
