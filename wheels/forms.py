from django import forms

Categories = (
        ('Alloy Repair', 'Alloy Repair'),
        ('Alloy Refurbish', 'Alloy Refurbish'),
        ('Alloy Colour', 'Alloy Colour'),
        ('Tyre Repair', 'Tyre Repair'),
        )

class NameForm(forms.Form):
	choice = forms.ChoiceField(choices=Categories)
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
	mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern' : '-?[0-9]*(\.[0-9]+)?'}))
	car_make = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
	model = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
	year = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern' : '-?[0-9]*(\.[0-9]+)?'}))
