from django import forms

class XMLForm(forms.Form):
    xml_link = forms.CharField(label='Enter your XML link here', max_length=100)