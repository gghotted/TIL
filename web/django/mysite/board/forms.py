from django.forms import ModelForm, ValidationError
from . import models


# custom validator
def validator(value):
    if len(value) <= 5:
        raise ValidationError('너무 짧아요.')


class BoardForm(ModelForm):
    class Meta:
        model = models.Board
        fields = ['title', 'text']

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators = [validator]
