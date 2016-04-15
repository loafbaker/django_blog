from django import forms

from datetime import date
from pagedown.widgets import PagedownWidget

from .models import Post

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(initial=date.today(), widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
			'image',
			'draft',
			'publish',
		]
