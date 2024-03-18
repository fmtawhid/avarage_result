# example/views.py
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    

   return render(request, 'index.html')

def fourth(request):
    context = {}  # Initialize the context dictionary

    if request.method == 'POST':  # Use 'POST' instead of 'post'
        n1 = float(request.POST.get('first', 0))  # Use request.POST.get() to avoid KeyError
        n2 = float(request.POST.get('second', 0))  # Use request.POST.get() to avoid KeyError
        n3 = float(request.POST.get('third', 0))  # Use request.POST.get() to avoid KeyError
        n4 = float(request.POST.get('fourth', 0))  # Use request.POST.get() to avoid KeyError

        #Calculate per sesult
        n1 = (n1*5)/100
        n2 = (n2*5)/100
        n3 = (n3*5)/100
        n4 = (n4*10)/100

        result = n1 + n2 + n3 + n4
        context['result'] = result

    return render(request, '4th.html', context)
def fifth(request):
    context = {}  # Initialize the context dictionary

    if request.method == 'POST':  # Use 'POST' instead of 'post'
        n1 = float(request.POST.get('first', 0))  # Use request.POST.get() to avoid KeyError
        n2 = float(request.POST.get('second', 0))  # Use request.POST.get() to avoid KeyError
        n3 = float(request.POST.get('third', 0))  # Use request.POST.get() to avoid KeyError
        n4 = float(request.POST.get('fourth', 0))  # Use request.POST.get() to avoid KeyError
        n5 = float(request.POST.get('fifth', 0))  # Use request.POST.get() to avoid KeyError

        #Calculate per result
        n1 = (n1*5)/100
        n2 = (n2*5)/100
        n3 = (n3*5)/100
        n4 = (n4*10)/100
        n5 = (n5*15)/100


        result = n1 + n2 + n3 + n4 + n5
        context['result'] = result

    return render(request, '5th.html', context)

def six(request):
    context = {}  # Initialize the context dictionary

    if request.method == 'POST':  # Use 'POST' instead of 'post'
        n1 = float(request.POST.get('first', 0))  # Use request.POST.get() to avoid KeyError
        n2 = float(request.POST.get('second', 0))  # Use request.POST.get() to avoid KeyError
        n3 = float(request.POST.get('third', 0))  # Use request.POST.get() to avoid KeyError
        n4 = float(request.POST.get('fourth', 0))  # Use request.POST.get() to avoid KeyError
        n5 = float(request.POST.get('fifth', 0))  # Use request.POST.get() to avoid KeyError
        n6 = float(request.POST.get('six', 0))  # Use request.POST.get() to avoid KeyError

        #Calculate per result
        n1 = (n1*5)/100
        n2 = (n2*5)/100
        n3 = (n3*5)/100
        n4 = (n4*10)/100
        n5 = (n5*15)/100
        n6 = (n6*20)/100


        result = n1 + n2 + n3 + n4 + n5 + n6
        context['result'] = result

    return render(request, '6th.html', context)
def seven(request):
    context = {}  # Initialize the context dictionary

    if request.method == 'POST':  # Use 'POST' instead of 'post'
        n1 = float(request.POST.get('first', 0))  # Use request.POST.get() to avoid KeyError
        n2 = float(request.POST.get('second', 0))  # Use request.POST.get() to avoid KeyError
        n3 = float(request.POST.get('third', 0))  # Use request.POST.get() to avoid KeyError
        n4 = float(request.POST.get('fourth', 0))  # Use request.POST.get() to avoid KeyError
        n5 = float(request.POST.get('fifth', 0))  # Use request.POST.get() to avoid KeyError
        n6 = float(request.POST.get('six', 0))  # Use request.POST.get() to avoid KeyError
        n7 = float(request.POST.get('seven', 0))  # Use request.POST.get() to avoid KeyError

        #Calculate per result
        n1 = (n1*5)/100
        n2 = (n2*5)/100
        n3 = (n3*5)/100
        n4 = (n4*10)/100
        n5 = (n5*15)/100
        n6 = (n6*20)/100
        n7 = (n7*25)/100


        result = n1 + n2 + n3 + n4 + n5 + n6 + n7
        context['result'] = result

    return render(request, '7th.html', context)

def eight(request):
    context = {}  # Initialize the context dictionary

    if request.method == 'POST':  # Use 'POST' instead of 'post'
        n1 = float(request.POST.get('first', 0))  # Use request.POST.get() to avoid KeyError
        n2 = float(request.POST.get('second', 0))  # Use request.POST.get() to avoid KeyError
        n3 = float(request.POST.get('third', 0))  # Use request.POST.get() to avoid KeyError
        n4 = float(request.POST.get('fourth', 0))  # Use request.POST.get() to avoid KeyError
        n5 = float(request.POST.get('fifth', 0))  # Use request.POST.get() to avoid KeyError
        n6 = float(request.POST.get('six', 0))  # Use request.POST.get() to avoid KeyError
        n7 = float(request.POST.get('seven', 0))  # Use request.POST.get() to avoid KeyError
        n8 = float(request.POST.get('eight', 0))  # Use request.POST.get() to avoid KeyError

        #Calculate per result
        n1 = (n1*5)/100
        n2 = (n2*5)/100
        n3 = (n3*5)/100
        n4 = (n4*10)/100
        n5 = (n5*15)/100
        n6 = (n6*20)/100
        n7 = (n7*25)/100
        n8 = (n8*15)/100


        result = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8

        context={
            "result":result,
        }

    return render(request, '8th.html', context)
