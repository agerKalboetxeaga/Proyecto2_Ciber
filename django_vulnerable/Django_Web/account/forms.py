from django import forms

from account.models import usuario

class PostForm(forms.ModelForm):

    class Meta:
        model = usuario
        fields = ('username', 'password',)