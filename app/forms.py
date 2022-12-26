from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['name','topic_name']
        #exclude=['name']
        help_texts={'topic_name':'should not be integer','name':'only alphabets'}
        labels={'topic_name':'TN','name':'N'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}


class AccessRecordsForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'