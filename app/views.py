from django.shortcuts import render


def homepage(request):
    #homepage view
    return render(request,'homepage.html',locals())

def about(request):
    #homepage view
    return render(request,'about.html',locals())

def service(request):
    #homepage view
    return render(request,'service.html',locals())

def contact(request):
    #homepage view
    return render(request,'contact.html',locals())

