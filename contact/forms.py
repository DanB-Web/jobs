from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    # Disable browser validation
    use_required_attribute = False
   
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Name', 'class': 'form-control'}
    ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter Email', 'class': 'form-control'}
    ))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Your message', 'class': 'form-control'}
    ))
   
    class Meta:
      model = Contact
      fields = ['name', 'email', 'message']

    # Custom validation for specific field
    def clean_message(self):
       message = self.cleaned_data.get('message')
       if (len(message) < 10):
          raise forms.ValidationError('Please enter a longer message')
       return message