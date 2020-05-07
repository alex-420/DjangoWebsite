from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# The class below is used to save user information when they register on the site.
# The fields have been selected to allow users the most privacy.
#2 password fields have been used to ensure maximum security for the user.

class RegisterUserForm(UserCreationForm):

    class Meta:
        fields = ('username','first_name','last_name','email','password1','password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Email Address'
