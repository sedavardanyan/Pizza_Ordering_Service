from django.shortcuts import render


def create(request):
    return render(request, 'orders/create.html')


def update(request):
    return render(request, 'orders/update.html')


def remove(request):
    return render(request, 'orders/remove.html')


def list_all(request):
    return render(request, 'orders/list.html')
