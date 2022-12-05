from django import forms
from .models import Customer,Mistriuser
from django.db import transaction 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerUserForm(UserCreationForm):
    name=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User


    @transaction.atomic
    def data_save(self):
        user=super().save(commit=False)
        user.save()
        customer=Customer.objects.create(user=user)
        customer.name=self.cleaned_data.get('name')
        customer.save()
        return user


class MistriuserForm(UserCreationForm):
    name=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User


    @transaction.atomic
    def data_save(self):
        user=super().save(commit=False)
        user.save()
        mistri=Mistriuser.objects.create(user=user)
        mistri.name=self.cleaned_data.get('name')
        mistri.save()
        return user
