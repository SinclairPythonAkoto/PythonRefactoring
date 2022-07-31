from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()  # the variable name will get sent to the form page
