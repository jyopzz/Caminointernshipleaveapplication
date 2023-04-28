from django.forms import ModelForm
from django import forms
from .models import *

class Adminform(ModelForm):
    class Meta:
        model = Admindata
        fields =   '__all__'