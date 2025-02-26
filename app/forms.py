from django import forms
from .models import Video, Comment, User, Card, Wallet


class CardForm(forms.Form):
    number = forms.CharField(label="Card Number", required=True)
    expiration_date = forms.DateField(label="Expiration Date", required=True)
    cvv = forms.CharField(label="CVV", required=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label="Username", required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=64, label="Username", required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirmation = forms.CharField(widget=forms.PasswordInput, required=True)


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "description", "video"]

    widgets = {
        "creator": forms.HiddenInput(),
        "description": forms.Textarea(attrs={"rows": 4, "cols": 15}),
    }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class PicureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar"]
