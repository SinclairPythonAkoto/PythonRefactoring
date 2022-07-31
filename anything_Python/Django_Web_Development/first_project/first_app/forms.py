from xmlrpc.client import boolean
from django import forms


# class SearchForm(forms.Form):
#     q = forms.CharField()  # the variable name will get sent to the form page


class TestForm(forms.Form):
    text = forms.CharField(max_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()
