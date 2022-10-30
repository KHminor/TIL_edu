from .models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'