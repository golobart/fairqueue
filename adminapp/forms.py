from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Resource


class SearchRscsForm(forms.Form):
    rsc_name = forms.CharField(label= _('Name'),max_length=20, required=False,
                               widget=forms.TextInput(attrs={'autofocus': '',
                                                             'placeholder': _('Resource name')}))
    rsc_desc = forms.CharField(label= _('Description'), max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Resource description')}))
    cal_name = forms.CharField(label= _('Calendar'), max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Calendar name')}))


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        # fields = ['name', 'description', 'text_title', 'calendar']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'autofocus': '', 'placeholder': _('Resource name')}),
            'description': forms.TextInput(attrs={'placeholder': _('Resource description')}),
            'text_title': forms.TextInput(attrs={'placeholder': _('Resource title')}),
        }
