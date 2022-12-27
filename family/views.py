from django.shortcuts import render
from django.http import HttpResponse
from family.models import Familiar

def create_familiar(request):
    new_familiar= Familiar.objects.create(name= 'Liz', years= 16, married= False)
    return HttpResponse('Se ha añadido un nuevo familiar')

def list_familiar(request):
    all_family = Familiar.objects.all()
    print(all_family)
    context={
        'family':all_family,
    }
    return render(request, 'list_family.html', context=context)