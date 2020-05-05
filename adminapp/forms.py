from django import forms

class SearchRscsForm(forms.Form):
    rsc_name = forms.CharField(label='Name',max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': 'Resource name'}))
    rsc_desc = forms.CharField(label='Description', max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Resource description'}))
