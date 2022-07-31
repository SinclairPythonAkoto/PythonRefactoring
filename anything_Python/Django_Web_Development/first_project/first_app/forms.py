from xmlrpc.client import boolean
from django import forms


# class SearchForm(forms.Form):
#     q = forms.CharField()  # the variable name will get sent to the form page


class TestForm(forms.Form):
    text = forms.CharField(max_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()

    def clean_integer(self):
        integer = self.cleaned_data.get("integer")
        if integer <= 10:
            raise forms.ValidationError("The integer must be greater than 10.")
        return integer
