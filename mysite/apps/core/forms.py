from django import forms
from core.models import Post

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', )


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)