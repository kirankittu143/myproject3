from django.shortcuts import render

# Create your views here.

def a2_first(request):
    d={'a':13455,'b':4532,'c':5678}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'a':455,'b':4532,'c':50678}
    return render(request,'a2_second.html',d)