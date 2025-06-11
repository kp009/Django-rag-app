from django import forms

class UploadForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    query = forms.CharField()