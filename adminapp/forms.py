from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Resource


class SearchRscsForm(forms.Form):
    ORDER_BY = [('asc', _('asc.')),
               ('des', _('desc.')),
               ('no', _('no'))]

    rsc_name = forms.CharField(label= _('Name'),max_length=20, required=False,
                               widget=forms.TextInput(attrs={'autofocus': '',
                                                             'placeholder': _('Resource name')}))
    ord_name = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    rsc_desc = forms.CharField(label= _('Description'), max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Resource description')}))
    ord_desc = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    cal_name = forms.CharField(label= _('Calendar'), max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Calendar name')}))
    ord_cal_name = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')


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
