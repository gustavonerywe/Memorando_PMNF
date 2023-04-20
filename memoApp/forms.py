from .models import Image
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'file')

    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))