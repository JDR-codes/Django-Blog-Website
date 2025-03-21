from django import forms

class ProfileForm(forms.Form):
    profile = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea())
    phone_number = forms.IntegerField()