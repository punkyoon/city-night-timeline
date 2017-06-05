from django import forms

from service.models import Timeline

class MessageForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                #'class': 'form-control',
                'placeholder': 'message',
            }
        )
    )

class SearchForm(forms.Form):
    date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                #'class': 'form-control',
            }
        )
    )
