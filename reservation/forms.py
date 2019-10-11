from django import forms
from .models import Reservation

class ReservationPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'p_name', 'start_date', 'end_date', 'people', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['p_name'].label = "입금자 명"
        self.fields['p_name'].widget.attrs = {'class': "form-control", 'placeholder': "입금자 명을 입력해주세요"}

        self.fields['start_date'].label = "시작시간"
        self.fields['start_date'].widget = forms.DateInput(format='2019-10-10 10:00')
        self.fields['start_date'].widget.attrs = {'class': "form-control", 'placeholder': ""}

        self.fields['end_date'].label = "종료시간"
        self.fields['end_date'].widget = forms.DateInput(format='2019-10-10 12:00')
        self.fields['end_date'].widget.attrs = {'class': "form-control", 'placeholder': ""}

        self.fields['people'].label = "인원"
        self.fields['people'].widget.attrs = {'class': "form-control", 'placeholder': ""}

        self.fields['password'].label = "비밀번호"
        self.fields['password'].widget = forms.PasswordInput()
