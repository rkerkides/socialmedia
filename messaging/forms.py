from django import forms
from django.contrib.auth import get_user_model

class SendMessageForm(forms.Form):
    receiver = forms.ModelChoiceField(queryset=get_user_model().objects.all(), label="To")
    content = forms.CharField(widget=forms.Textarea, label="Message")

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        # Custom initialization can be done here, if necessary
