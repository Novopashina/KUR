from django import forms
from .models import Image
from .models import Feedback

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','image')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'topic', 'message']