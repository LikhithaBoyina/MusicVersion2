from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

# class CreateUserForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#             visible.field.widget.attrs['id'] = 'exampleInputEmail'
#             visible.field.widget.attrs['placeholder'] = visible.field.label
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']


# class AlbumForm(ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'

# class SongForm(ModelForm):
#     class Meta:
#         model = Song
#         fields = '__all__'