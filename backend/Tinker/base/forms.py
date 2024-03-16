from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InventoryItem

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = "__all__"

class InventoryItemForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=InventoryItem.objects.all(), initial=0)
	class Meta:
		model = InventoryItem
		fields = "__all__"
