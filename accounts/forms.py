from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			# 1. First check if user exists
			user_exists = User.objects.filter(username=username).exists()
			if not user_exists:
				raise forms.ValidationError('This user does not exist.')
			# 2. Second check if user password is correct
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('Incorrect password.')
			if not user.is_active:
				raise forms.ValidationError('This user is no longer active.')
		return super(UserLoginForm, self).clean()


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')
	email2 = forms.EmailField(label='Confirm Email')
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
			'password2',
		]

	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError('The input emails should match.')
		email_exists = User.objects.filter(email=email).exists()
		if email_exists:
			raise forms.ValidationError('This email has been already registered.')
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Passwords do not match')
		return password2