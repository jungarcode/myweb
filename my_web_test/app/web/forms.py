from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'write your name'}), min_length=3,max_length=100)
    email = forms.EmailField(label="Email Address",required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'write your email'}),min_length=3,max_length=100)
    contact = forms.CharField(label="Message",required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'write your message'}),min_length=10,max_length=1000)