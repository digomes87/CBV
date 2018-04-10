from django import forms
from .models import Cadastro


class form_cadastro(forms.ModelForm):
	nome = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control',})
	)

	idade = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control'})
	)

	descricao = forms.CharField(widget=forms.Textarea(
		attrs={'class':'form-control'}
	))
	class Meta:
		model = Cadastro
		fields = ["nome", "idade", "descricao"]

	def clean(self, *args, **kwargs):
		cleaned_data = super(form_cadastro, self).clean(*args, **kwargs)
