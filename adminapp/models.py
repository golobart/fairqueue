from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator


class Calendar(models.Model):
    owner = models.CharField( _('Calendar owner'), max_length=200)
    name = models.CharField( _('Calendar name'), max_length=200)
    description = models.CharField( _('Calendar description'), max_length=200, null=True, blank=True)
    year = models.DecimalField( _('Calendar year'), max_digits=4, decimal_places=0, null=True, blank=True)
    ini_day = models.DateField( _('Calendar first day'),
                                help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    end_day = models.DateField( _('Calendar last day'))
    template = models.BooleanField( _('Is calendar template'))
    next = models.ForeignKey('self', on_delete=models.PROTECT, related_name='next_cal', null=True, blank=True, verbose_name=_('Next Calendar') )
    prev = models.ForeignKey('self', on_delete=models.PROTECT, related_name='prev_cal', null=True, blank=True, verbose_name=_('Previous Calendar'))
    open = models.BooleanField( _('Is calendar open'))

    def __str__(self):
        return self.name


class DaysOff(models.Model):
    DAY = 'DA'
    DAYS_RANGE = 'DR'
    WEEK_DAY = 'WD'
    MONTH_DAY = 'MD'
    MONTH = 'MO'
    TYPE_OF_DAY_CHOICES = [
        (DAY, _('Single day')),
        (DAYS_RANGE, _('Range of days')),
        (WEEK_DAY, _('Day of week')),
        (MONTH_DAY, _('Day of month')),
        (MONTH, _('Full month')),
    ]
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField( _('Days off name'), max_length=200)
    description = models.CharField( _('Days off description'), max_length=200, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_OF_DAY_CHOICES, default=DAY)
    day = models.DateField()
    end_day = models.DateField()
    week_day = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(7)])
    month_day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    from_day = models.DateField()
    to_day = models.DateField()

    def __str__(self):
        return self.name


class WorkingTime(models.Model):
    NORMAL = 'NO'
    INTERDAY = 'ID'
    MORE_24H = 'M2'
    TYPE_OF_SCHEDULE = [
        (NORMAL, _('Normal')),
        (INTERDAY, _('Interday scheduling')),
        (MORE_24H, _('More than 24 hours')),
    ]
    name = models.CharField( _('Working time name'), max_length=200)
    description = models.CharField( _('Working time description'), max_length=200, blank=True)
    ini_hour = models.CharField(max_length=200)
    end_hour = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=TYPE_OF_SCHEDULE, default=NORMAL)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField( _('Resource name'), max_length=200)
    description = models.CharField( _('Resource description'), max_length=200, blank=True, null=True)
    text_title = models.CharField( _('Resource title'), max_length=200, blank=True, null=True)
#    calendar = models.ForeignKey(Calendar, on_delete=models.SET_NULL, blank=True, null=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class CalendarDefWT(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    working_time = models.ForeignKey(WorkingTime, on_delete=models.CASCADE)
    granted_days = models.IntegerField( _('Number of days granted to be booked'))
    slot_minutes = models.IntegerField( _('Duration in minutes of each booking slot'))


class DaySpecWT(models.Model):
    DAY = 'DA'
    DAYS_RANGE = 'DR'
    WEEK_DAY = 'WD'
    MONTH_DAY = 'MD'
    MONTH = 'MO'
    TYPE_OF_DAY_CHOICES = [
        (DAY, _('Single day')),
        (DAYS_RANGE, _('Range of days')),
        (WEEK_DAY, _('Day of week')),
        (MONTH_DAY, _('Day of month')),
        (MONTH, _('Full month')),
    ]
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    working_time = models.ForeignKey(WorkingTime, on_delete=models.CASCADE)
    slot_minutes = models.IntegerField( _('Duration in minutes of each booking slot'))
    type = models.CharField(max_length=2, choices=TYPE_OF_DAY_CHOICES, default=DAY)
    day = models.DateField()
    end_day = models.DateField()
    week_day = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(7)])
    month_day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    from_day = models.DateField()
    to_day = models.DateField()


