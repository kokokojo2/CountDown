from .models import Countdown
from django import forms


class CountdownForm(forms.ModelForm):

    class Meta:
        model = Countdown
        fields = ('name', 'description', 'finished')

    widgets = {'finished': forms.DateTimeInput(format='%Y-%m-%dT%H:%M')}
