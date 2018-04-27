from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Note
import random
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

'''
def hello(request):
    x = random.randint(1,100)
    html = "<h1>Hello, Django {}</h1>".format(x)
    return HttpResponse(html)
'''
def getRandom():
    return random.randint(1,100)

def hello(request):
    x = random.randint(1,100)
    v = {"value" : x}
    return render(request, 'simple/hello.html', {'data': v})

def note(request):
    notes = Note.objects.all().order_by('-published_date')
    return render(request, 'simple/memo.html', {'notes': notes})

class Write(CreateView):
    model = Note
    fields = ['name', 'text']
    success_url = reverse_lazy('note')