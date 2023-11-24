from django import forms
# from ckeditor.widgets import CKEditorWidget
from .models import News

class AddNewForm(forms.ModelForm):
    # title = forms.CharField(max_length=255)
    # img =  forms.ImageField()
    # body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = News
        fields = ['title', 'img', 'body', 'category', 'tags', 'is_active']
