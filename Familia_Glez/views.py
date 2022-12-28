from django.http import HttpResponse
from django.shortcuts import render

def nombre_familiar(request):
    return HttpResponse("Lista de Familiares de Katya Gonzalez")

def vista_con_template(request):
    return render(request, 'Template.html', context={})