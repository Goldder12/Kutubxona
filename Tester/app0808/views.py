from django.shortcuts import render,redirect
from .models import *

def todo1(request ):
    hamma = Todo.objects.all()
    data={
        'todo' : hamma
    }
    return render(request,'todo.html', data)
def ochirish(request, son):
    Todo.objects.get(id=son).delete()
    return redirect('/todo/')
