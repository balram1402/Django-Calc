from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"calc.html")

def adds(request):
    val1a = int(request.GET['text1'])
    val2a = int(request.GET['text2'])

    result = val1a + val2a
    return render(request,"result.html",{'result':result})

def sub(request):
    val1a = int(request.GET['text1s'])
    val2a = int(request.GET['text2s'])

    result = val1a - val2a
    return render(request,"result.html",{'result':result})

def mul(request):
    val1a = int(request.GET['text1m'])
    val2a = int(request.GET['text2m'])

    result = val1a * val2a
    return render(request,"result.html",{'result':result})

def div(request):
    val1a = int(request.GET['text1d'])
    val2a = int(request.GET['text2d'])

    result = val1a / val2a
    return render(request,"result.html",{'result':result})


