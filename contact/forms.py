from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)