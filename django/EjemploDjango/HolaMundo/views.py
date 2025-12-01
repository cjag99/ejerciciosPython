from django.shortcuts import HttpResponse
from django.shortcuts import render
# Create your views here.
def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo desde Django</h1>")

def home(request):
    return render(request, 'index.html')