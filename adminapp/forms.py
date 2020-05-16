from django import forms
from .models import Resource


class SearchRscsForm(forms.Form):
    rsc_name = forms.CharField(label='Name',max_length=20, required=False,
                               widget=forms.TextInput(attrs={'autofocus': '',
                                                             'placeholder': 'Resource name'}))
    rsc_desc = forms.CharField(label='Description', max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Resource description'}))
    cal_name = forms.CharField(label='Calendar', max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Calendar name'}))


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        # fields = ['name', 'description', 'text_title', 'calendar']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'autofocus': ''}),
        }
