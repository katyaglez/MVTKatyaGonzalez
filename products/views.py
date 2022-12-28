from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products

def create_familiar(request):
    new_familiar= Products.objects.create(nombre='Antonino', apellido='Espinoza', edad=73, esta_vivo=False)
    print(new_familiar)
    return HttpResponse('Se creo el nuevo Familiar')

def list_familiar(request):
    all_familiar = Products.objects.all()
    print(all_familiar)
    context = {
        'Familia':all_familiar,
    }
    return render(request,'list_familiar.html',context=context)