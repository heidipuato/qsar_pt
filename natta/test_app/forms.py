from django import forms
from .models import *
from django.db import models
from django.db.models import fields
from django.forms import NumberInput
from django.forms import widgets, ModelForm, Select

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = "__all__"
        widgets = {
            'val1':  NumberInput(attrs={'class': 'form-control'}),
            'val2':  NumberInput(attrs={'class': 'form-control'}),
            'val3':  NumberInput(attrs={'class': 'form-control'}),
            'val4':  NumberInput(attrs={'class': 'form-control'}),
            'val5':  NumberInput(attrs={'class': 'form-control'}),
            'val6':  NumberInput(attrs={'class': 'form-control'}),
            'val7':  NumberInput(attrs={'class': 'form-control'}),
            'val8':  NumberInput(attrs={'class': 'form-control'}),
            'val9':  NumberInput(attrs={'class': 'form-control'}),
            'val10':  NumberInput(attrs={'class': 'form-control'}),
        }

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"
        widgets = {
            'np':  Select(attrs={'class': 'form-control'}),
            'me':  Select(attrs={'class': 'form-control'}),
            'bt':  Select(attrs={'class': 'form-control'}),
            'ns':  Select(attrs={'class': 'form-control'}),
            'dm':  Select(attrs={'class': 'form-control'}),
            'ta':  Select(attrs={'class': 'form-control'}),
            'sc':  Select(attrs={'class': 'form-control'}),
            'f1':  NumberInput(attrs={'class': 'form-control'}),
            'f2':  NumberInput(attrs={'class': 'form-control'}),
            'f3':  NumberInput(attrs={'class': 'form-control'}),
            'f4':  NumberInput(attrs={'class': 'form-control'}),
            'f5':  NumberInput(attrs={'class': 'form-control'}),
            'f6':  NumberInput(attrs={'class': 'form-control'}),
            'f7':  NumberInput(attrs={'class': 'form-control'}),
            'f8':  NumberInput(attrs={'class': 'form-control'}),
            'f9':  NumberInput(attrs={'class': 'form-control'}),
            'f10':  NumberInput(attrs={'class': 'form-control'}),
        }