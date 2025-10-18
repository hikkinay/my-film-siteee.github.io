from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date', 'image']



        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название фильма"
            }),
            "anons": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Анонс"
            }),
            "date": DateTimeInput(attrs={
                'class': "form-control",
                'type': "datetime-local",
            }),
            "full_text": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Описание произведения"
            }),

            "image": FileInput(attrs={'class': "form-control"}),

        }



from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий...'
            }),
        }
