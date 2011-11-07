from django.forms import DateInput

from apps.input_mask.widgets import InputMask


class DateMask(InputMask, DateInput):
    mask = "{mask:'99/99/9999'}"
