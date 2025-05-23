from django import forms
from .models import Page
from django_ckeditor_5.widgets import CKEditor5Widget

class PageForm(forms.ModelForm):

    class Meta:
        model= Page
        fields=['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="default"),
            'order': forms.NumberInput(attrs={'class':'form-control'})
    }
