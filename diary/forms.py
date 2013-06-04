from django import forms

class DiaryForm(forms.Form):
	date = forms.DateField()
	content = forms.CharField(widget=forms.Textarea)