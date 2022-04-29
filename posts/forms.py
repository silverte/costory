from django import forms
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=50, label='제목')
#     content = forms.CharField(label='내용', widget=forms.Textarea)

class PostForm(forms.ModelForm):
    #memo = forms.CharField(max_length=80, validators=[validate_symbols], required=False)

    class Meta:
        model = Post
        fields = ['title','content']
        #fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={
                'class': 'title',
                'placeholder': '제목을 입력 하세요'}),
            'content': forms.Textarea(attrs={
                'placeholder': '내용을 입력 하세요'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다.')
        return title