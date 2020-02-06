from django import forms

from app.models import Post


class SimpleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
