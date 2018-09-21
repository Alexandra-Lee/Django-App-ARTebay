from django import forms

class ShowForm(forms.Form):
    title = forms.CharField(required=False, max_length=100, help_text='120 characters max.')
    venue = forms.CharField(required=True, max_length=70, help_text='name of museum, gallery, or venue')
    description = forms.CharField(required=True, widget=forms.Textarea)
    contact_email = forms.EmailField(required=True, help_text="Contact/Info email")