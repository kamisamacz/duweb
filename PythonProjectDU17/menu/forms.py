from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)