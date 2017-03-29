from django.shortcuts import render
from hsdm.models import *
def home(req):
    return render(req,'home.html')
def id1101(req):
    return render(req,'id1101.html')
