from django import forms
from . models import cont


class TaskForm(forms.ModelForm):
    class Meta:
        model=cont
        fields=['fname','lname','email','message']
        widgets={
            'fname':forms.TextInput(attrs={
                'placeholder':'enter fristname',
                'required':'required',
            }),
              'lname':forms.TextInput(attrs={
                'placeholder':'enter lastname',
                'required':'required',
            }),
              'email':forms.TextInput(attrs={
                'placeholder':'enter email',
                'required':'required',
            }),
              'message':forms.TextInput(attrs={
                'placeholder':'enter message',
                'required':'required',
            }),

        }


