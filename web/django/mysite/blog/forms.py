from django.forms import ModelForm, CharField, Textarea, ValidationError
from .models import Post


# custom validator
def validator(value):
    if len(value) <= 5:
        raise ValidationError('너무 짧아요.')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']