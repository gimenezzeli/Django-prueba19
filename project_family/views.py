from django.http import HttpResponse
from django.shortcuts import render

def vista_template(request):
    return render(request, 'template.html', context={})