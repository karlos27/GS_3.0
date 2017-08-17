from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField()
    correu = forms.EmailField()
    telf = forms.CharField(required=False)
    missatge = forms.CharField(widget=forms.Textarea)

   