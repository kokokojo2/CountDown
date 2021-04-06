from .models import Countdown
from django import forms


class CountdownForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Countdown
        fields = ('name', 'description', 'finished_text', 'finished')

    widgets = {'finished': forms.DateTimeInput(format='%Y-%m-%dT%H:%M')}
