from django import forms
from django.utils.dates import WEEKDAYS, MONTHS
from django.utils.translation import ugettext_lazy as _

from .models import Resource, Calendar, WorkingTime, DaysOff


class SearchRscsForm(forms.Form):
    ORDER_BY = [('asc', _('asc.')),
               ('des', _('desc.')),
               ('no', _('no'))]

    rsc_name = forms.CharField(label= _('Name'),max_length=200, required=False,
                               widget=forms.TextInput(attrs={'autofocus': '',
                                                             'placeholder': _('Resource name')}))
    ord_name = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='asc')
    rsc_desc = forms.CharField(label= _('Description'), max_length=200, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Resource description')}))
    ord_desc = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    cal_name = forms.CharField(label= _('Calendar'), max_length=200, required=False,
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


class SearchCalsForm(forms.Form):
    ORDER_BY = [('asc', _('asc.')),
               ('des', _('desc.')),
               ('no', _('no'))]

    cal_owner = forms.CharField(label= _('Owner'),max_length=200, required=False,
                               widget=forms.TextInput(attrs={'autofocus': '',
                                                             'placeholder': _('Calendar owner')}))
    ord_owner = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    cal_name = forms.CharField(label= _('Name'), max_length=200, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Calendar name')}))
    ord_name = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='asc')
    cal_desc = forms.CharField(label= _('Description'), max_length=200, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Calendar description')}))
    ord_desc = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

    cal_year = forms.DecimalField(label= _('Year'), max_digits=4, decimal_places=0, required=False,
                               widget=forms.NumberInput(attrs={'placeholder': _('Year')}))
    ord_year = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

    # TODO es podria fer un filtre per tots els camps
    # cal_ini_day = forms.DateField (label= _('First day'), required=False,
    #                            widget=forms.TextInput(attrs={'placeholder': _('Calendar first day')}))
    # ord_ini_day = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    # cal_end_day = forms.DateField (label= _('Last day'), required=False,
    #                            widget=forms.TextInput(attrs={'placeholder': _('Calendar last day')}),
    #                            help_text="Please use the following formaat: <em>YYYY-MM-DD</em>.")
    # ord_end_day = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    #
    # cal_template = forms.BooleanField(label= _('Template'), required=False,
    #                                   help_text="Can the calendar be used as a template for others calendars?")
    # ord_template = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    #
    # cal_prev = forms.CharField(label= _('Previous calendar'), max_length=200, required=False,
    #                            widget=forms.TextInput(attrs={'placeholder': _('Previous calendar name')}))
    # ord_prev = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    # cal_next = forms.CharField(label= _('Next calendar'), max_length=200, required=False,
    #                            widget=forms.TextInput(attrs={'placeholder': _('Next calendar name')}))
    # ord_next = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')
    #
    # cal_open = forms.BooleanField(label= _('Open'), required=False,
    #                                   help_text="Is the calendar open to be used?")
    # ord_open = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'
        widgets = {
            'owner': forms.TextInput(attrs={'autofocus': '', 'placeholder': _('Calendar owner name')}),
            'name': forms.TextInput(attrs={'placeholder': _('Calendar name')}),
            'description': forms.TextInput(attrs={'placeholder': _('Calendar description')}),
            'year': forms.NumberInput(attrs={'placeholder': _('Year')}),
            'ini_day': forms.DateInput(attrs={'placeholder': _('Calendar first day')}),
            'end_day': forms.DateInput(attrs={'placeholder': _('Calendar last day')}),
            # 'template': forms.CheckboxInput(),
            #'next': forms.TextInput(attrs={'placeholder': _('Next calendar name')}),
            #'prev': forms.TextInput(attrs={'placeholder': _('Previous calendar name')}),
            # 'open': forms.CheckboxInput(),
        }


class SearchWTsForm(forms.Form):
    ORDER_BY = [('asc', _('asc.')),
               ('des', _('desc.')),
               ('no', _('no'))]
    sched = [('','--------')] + WorkingTime.TYPE_OF_SCHEDULE

    wt_name = forms.CharField(label= _('Name'), max_length=200, required=False,
                              widget=forms.TextInput(attrs={'placeholder': _('Working time name')}))
    ord_name = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='asc')
    wt_desc = forms.CharField(label= _('Description'), max_length=200, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Working time description')}))
    ord_desc = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

    wt_ini_hour = forms.CharField(label= _('Initial hour'), max_length=5, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Working time initial hour hh:mm')}))
    ord_ini_hour = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

    wt_end_hour = forms.CharField(label= _('Final hour'), max_length=5, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Working time ending hour hh:mm')}))
    ord_end_hour = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

    wt_type = forms.CharField(label= _('Type'), max_length=2, required=False,
                              widget=forms.Select(choices=sched))
    ord_type = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

class WorkingTimeForm(forms.ModelForm):
    class Meta:
        model = WorkingTime
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Working time name')}),
            'description': forms.TextInput(attrs={'placeholder': _('Working time description')}),
            'ini_hour': forms.TextInput(attrs={'placeholder': _('WT initial hour hh:mm')}),
            'end_hour': forms.TextInput(attrs={'placeholder': _('WT final hour hh:mm')}),
            'type': forms.RadioSelect(),
        }


class SearchDOsForm(forms.Form):
    ORDER_BY = [('asc', _('asc.')),
               ('des', _('desc.')),
               ('no', _('no'))]

    do_name = forms.CharField(label= _('Name'), max_length=200, required=False,
                              widget=forms.TextInput(attrs={'placeholder': _('Working time name')}))
    ord_name = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='asc')
    do_desc = forms.CharField(label= _('Description'), max_length=200, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Working time description')}))
    ord_desc = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

    do_type = forms.CharField(label= _('Day off type'), max_length=5, required=False,
                               widget=forms.Select(choices=DaysOff.TYPE_OF_DAY_CHOICES))
    ord_type = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')

    do_day = forms.DateField(label= _('Day'), required=False,
                               widget=forms.DateInput())
    ord_day = forms.ChoiceField(label='', choices=ORDER_BY, widget=forms.RadioSelect, initial='no')


    # name = models.CharField( _('Days off name'), max_length=200)
    # description = models.CharField( _('Days off description'), max_length=200, blank=True)
    # type = models.CharField(max_length=2, choices=TYPE_OF_DAY_CHOICES, default=DAY)
    # day = models.DateField()
    # end_day = models.DateField()
    # week_day = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    # month_day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    # month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    # from_day = models.DateField()
    # to_day = models.DateField()


class DaysOffForm(forms.ModelForm):
    class Meta:
        # django.utils.dates.WEEKDAYS and MONTHS int are not iterables
        model = DaysOff
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Days off name')}),
            'description': forms.TextInput(attrs={'placeholder': _('Days off description')}),
            #'type': forms.Select(choices=DaysOff.TYPE_OF_DAY_CHOICES),
            #'day': forms.SelectDateWidget(),
            'end_day': forms.SelectDateWidget(),
            'week_day': forms.Select(choices=DaysOff.WEEKDAY_CHOICES), # Monday='MO' ...
            'month': forms.Select(choices=DaysOff.MONTH_CHOICES), # January='JAN' ...
            'from_day': forms.DateInput(attrs={'type': 'Date'}),
            'to_day': forms.DateInput(),

        }
