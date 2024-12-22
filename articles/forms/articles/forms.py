from django import forms
from ...models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title', 'class': 'form-input'}),
            'author': forms.TextInput(attrs={'placeholder': "Author's name", 'class': 'form-input'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write the article content', 'class': 'form-textarea'}),
        }

