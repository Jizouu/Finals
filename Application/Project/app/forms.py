from django import forms
from .models import Post, Barangay, Service, UserProfile, Request

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

class BarangayForm(forms.ModelForm):
    class Meta:
        model = Barangay
        fields = ['name', 'address', 'contact_number']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'barangay']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'role', 'barangay']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['user', 'service', 'status']
