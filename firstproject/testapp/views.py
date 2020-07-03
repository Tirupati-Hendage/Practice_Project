from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def greeting(request):
    now=datetime.datetime.now()
    s="<h1>Hello and Welcome to first view of testapp, Its %s,</h1> <p>This is landing page</p>" %now
    return HttpResponse(s)

def showContact(request):
    s="<h1>Contact Page</h1>"
    s+="<p>Website:MySite.com</p>"
    s+="<p>Mobile:9359064463</p>"
    s+="<p>Email:hqtiru@gmail.com</p>"
    return HttpResponse(s)

def About(request):
    s="<h1>This is an about page</h1>"
    return HttpResponse(s)
