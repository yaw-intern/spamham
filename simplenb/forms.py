from django import forms

class classiy_form(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'u-full-width', 'placeholder':'Enter a message here'}), label='')