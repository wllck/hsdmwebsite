from django.shortcuts import render
from hsdm.models import *
from hsdm import forms
from django.core import serializers

def home(req):
    return render(req,'home.html')
def id1101(req):
    table_form = forms.UForm()
    id_form = Id1301GpsIntervalHe.objects.all()
    print(id_form)
    id_data = serializers.serialize("json",id_form)
    print(id_data)
    return render(req,'id1101.html',{'id_data':id_data})
