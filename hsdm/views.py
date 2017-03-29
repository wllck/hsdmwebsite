from django.shortcuts import render
from hsdm.models import *
from hsdm import forms
def home(req):
    return render(req,'home.html')
def id1101(req):
    table_form = forms.UForm()
    id1101_form = Id1301GpsIntervalHe.objects.all()
    return render(req,'id1101.html',locals())
