from django import forms
from .models import Post


# class SearchForm(forms.Form):
#     q = forms.CharField()  # the variable name will get sent to the form page
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["user", "title", "slug", "image", "content", "draft", "publish"]
        exclude = []


class TestForm(forms.Form):

    RADIO_CHOICES = [
        ("signin", "Sign In"),
        ("signup", "Sign Up"),
        ("forgotpasword", "Forgot Password"),
    ]
    INTS_CHOICES = [tuple([x, x]) for x in range(0, 100)]
    YEARS = [x for x in range(1980, 2031)]
    CHECKBOX_CHOICES = [
        ("terms", "Agree to the terms and conditions"),
        ("privacy", "Agree to pricavy policy"),
    ]

    date_field = forms.DateField(
        initial="2020-20-5", widget=forms.SelectDateWidget(years=YEARS)
    )
    text = forms.CharField(label="Feedback", min_length=7, widget=forms.Textarea)
    radio_choices = forms.CharField(widget=forms.RadioSelect(choices=RADIO_CHOICES))
    checkbox_choices = forms.CharField(
        widget=forms.CheckboxSelectMultiple(choices=CHECKBOX_CHOICES)
    )
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10, widget=forms.Select(choices=INTS_CHOICES))
    email = forms.EmailField()

    def clean_integer(self):
        integer = self.cleaned_data.get("integer")
        if integer <= 10:
            raise forms.ValidationError("The integer must be greater than 10.")
        return integer
