from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from user.models import User


class UserCreationForm(DjangoUserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("This email is already exists!")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match, Please Try again")

        return password2

    class Meta(DjangoUserCreationForm):
        model = User
        fields = (
            'username',
            'first_name',
            'supplier_address',
            'supplier_business_name',
            # 'last_name',
            'password1',
            'password2',
        )


class UpdateUserPrimaryForm(ModelForm):

    class Meta(DjangoUserCreationForm):
        model = User
        fields = (
            'first_name',
            'primary_phone'
        )


class UpdateUserSecondaryForm(ModelForm):

    class Meta(DjangoUserCreationForm):
        model = User
        fields = (
            'secondary_representative_name',
            'secondary_phone',
            'secondary_email'
        )
