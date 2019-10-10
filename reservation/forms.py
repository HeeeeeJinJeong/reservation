from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'p_name', 'start_date', 'end_date', 'people']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['p_name'].label = "입금자 명"

        self.fields['start_date'].label = "시작시간"
        self.fields['start_date'].widget = forms.DateInput(format='2019-10-10 10:00')

        self.fields['end_date'].label = "종료시간"
        self.fields['end_date'].widget = forms.DateInput(format='2019-10-10 12:00')

        self.fields['people'].label = "인원"