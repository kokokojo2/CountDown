from .models import Countdown
from django import forms

from .validators import positive_date_validator


class CountdownForm(forms.ModelForm):
    """
    This form is used to create a new Countdown object. Compatible with Bootstrap.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['description'].widget.attrs.update({'rows': "4", 'placeholder': ''})
        self.fields['finished_text'].widget.attrs.update({'rows': "4", 'placeholder': ''})

    class Meta:
        model = Countdown
        fields = ('name', 'description', 'finished_text', 'finished')

    widgets = {'finished': forms.DateTimeInput(format='%Y-%m-%dT%H:%M')}

    def clean(self):
        data = super(CountdownForm, self).clean()
        try:
            positive_date_validator(data['finished'])
        except KeyError:
            pass
