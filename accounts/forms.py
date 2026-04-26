from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User


class CustomUserCreationForm(forms.ModelForm):

    username = forms.CharField(max_length=150, required=True, label='نام کاربری')
    email = forms.EmailField(required=True, label='ایمیل')
    password1 = forms.CharField(widget=forms.PasswordInput, label='رمز عبور', min_length=4)
    password2 = forms.CharField(widget=forms.PasswordInput, label='تکرار رمز عبور')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # حذف اعتبارسنجی یکتایی نام کاربری - می‌تواند تکراری باشد
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('این ایمیل قبلاً ثبت شده است. لطفاً از ایمیل دیگری استفاده کنید.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # فقط بررسی حداقل ۴ کاراکتر
        if len(password1) < 4:
            raise ValidationError('رمز عبور باید حداقل ۴ کاراکتر باشد.')

        # هیچ اعتبارسنجی دیگری انجام نده
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('رمز عبور و تکرار آن مطابقت ندارند.')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user