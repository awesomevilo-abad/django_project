from django import forms
from first_app.models import User,UserProfileInfo
from django.contrib.auth.models import User
from django.core import validators

#----CUSTOM VALIDATOR------------
def check_for_z(value):
    if value[0].lower() != 'v':
        raise forms.ValidationError('Name Need to Start with Z')

class FormName(forms.Form):
    name = forms.CharField(validators = [check_for_z]) #Application of Custom validator check_for_z
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter you email again")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email is not match!")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Bot Found')
    #     return botcatcher

class StoreDetails(forms.Form):
    name = forms.CharField()
    code = forms.CharField()
    area = forms.IntegerField()
    location = forms.CharField(widget = forms.Textarea)

class NewUserForm(forms.ModelForm):
    # If Needed Validator will be in HERE
      # first_name = forms.CharField(validator=[])
    class Meta():
        model = User
        fields = '__all__' #Get All Fields in the Model

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
