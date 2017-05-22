from django import forms

from service.models import Timeline

class MessageForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'message',
            }
        )
    )
