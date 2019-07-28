from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


    def clean_first_name(self, *args, **kwargs):
        cleaned_data = super(ContactForm, self).clean
        first_name = self.cleaned_data.get('first_name')
        if(first_name.isupper()):
            raise forms.ValidationError("should be uppercase")
        return first_name

    def clean_last_name(self, *args, **kwargs):
        cleaned_data = super(ContactForm, self).clean
        last_name = self.cleaned_data.get('last_name')
        if(last_name.isupper()):
            raise forms.ValidationError("should be uppercase")
        return last_name





        