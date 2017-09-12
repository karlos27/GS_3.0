from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField()
    correu = forms.EmailField()
    telf = forms.CharField()
    missatge = forms.CharField(widget=forms.Textarea)

   