from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posts, Comments


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('user', 'title', 'content')


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('user', 'content')
