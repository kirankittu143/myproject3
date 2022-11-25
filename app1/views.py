from django.shortcuts import render

# Create your views here.

def a1_first(request):
    d={'a':77210,'b':3000,'c':400}
    return render(request,'a1_first.html',d)

def a1_second(request):
    d={'a':182,'b':531,'c':287}
    return render(request,'a1_second.html',d)