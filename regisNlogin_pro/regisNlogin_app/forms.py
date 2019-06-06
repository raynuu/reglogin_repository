from django import forms
from regisNlogin_app.models import registration,login

class registrationform(forms.ModelForm):
    class Meta:
        model=registration
        fields='__all__'

class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'



