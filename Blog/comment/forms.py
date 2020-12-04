from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': '昵称',
                'class': 'form-control form-control-lg',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'QQ邮箱',
                'class': 'form-control form-control-lg',
            }),
            'text': Textarea(attrs={
                'class': 'form-control', 'rows': 3,
                'id': 'exampleFormControlTextarea1',
                'placeholder': '留下你的足迹^_^'
            }),
        }
