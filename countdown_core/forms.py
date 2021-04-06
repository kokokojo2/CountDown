from .models import Countdown
from django import forms


class CountdownForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['description'].widget.attrs.update({'rows': "4",
                                                        'placeholder': ''}) #'Tell the people what this countdown is made for.'})

        self.fields['finished_text'].widget.attrs.update({'rows': "4",
                                                          'placeholder': ''}) #'This text will be displayed in the moment, when countdown is finished.'})

    class Meta:
        model = Countdown
        fields = ('name', 'description', 'finished_text', 'finished')

    widgets = {'finished': forms.DateTimeInput(format='%Y-%m-%dT%H:%M')}
