from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # Убедись, что эти поля (author, text, rating) есть в твоей модели Review
        fields = ['author', 'text', 'rating']

        labels = {
            'author': 'Ваше имя',
            'text': 'Ваш отзыв',
            'rating': 'Оценка гаджета',
        }

        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
                'style': 'background: #252525; color: white; border: 1px solid #444;'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Напишите, что вы думаете об этом устройстве...',
                'style': 'background: #252525; color: white; border: 1px solid #444;'
            }),
            'rating': forms.Select(
                choices=[(i, f'{i} ⭐') for i in range(5, 0, -1)],
                attrs={
                    'class': 'form-select',
                    'style': 'background: #252525; color: white; border: 1px solid #444;'
                }
            ),
        }