from django import forms

from service.models import Timeline

class SearchForm(forms.Form):
    date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                #'class': 'form-control',
            }
        )
    )
