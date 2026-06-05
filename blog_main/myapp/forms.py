from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'})
    )
    subject = forms.CharField(
        max_length=120,
        label='Subject',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'What would you like to say?'}),
    )
