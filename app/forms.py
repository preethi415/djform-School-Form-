from django import forms
class SchoolForm(forms.Form):
    sname=forms.CharField()
    sprincipal=forms.CharField()
    slocation=forms.CharField()
