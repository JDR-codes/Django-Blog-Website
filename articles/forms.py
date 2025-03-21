from django import forms
from . models import *

class ArticleForm(forms.Form):
    category = forms.ModelChoiceField(queryset= Category.objects.all())
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'rows' : 5, 'cols': 30}))

    def create(self,author):
        return Article.objects.create(
        category = self.cleaned_data['category'],
        title = self.cleaned_data['title'],
        content = self.cleaned_data['content'],
        author = author
        )
    
    def update(self,instance):
        instance.category = self.cleaned_data['category']
        instance.title = self.cleaned_data['title']
        instance.content = self.cleaned_data['content']
        instance.save()
        return instance

    
