from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()

    return render(request, "hello.html", {'name':'Stylianos '})

# Create a new view function called User_Profile to return a json response with the data; name, email and phone number
# Register the view function on a path called profile.