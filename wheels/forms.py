from django import forms

Categories = (
        ('Wheel Repair', 'Wheel Repair'),
        ('Wheel Refurbish', 'Wheel Refurbish'),
        ('Wheel Colour', 'Wheel Colour'),)

class NameForm(forms.Form):
	choice = forms.ChoiceField(label='Category', choices=Categories)
	name = forms.CharField(label='Name', max_length=25)
	mobile = forms.IntegerField(label='Mobile')
	car_make = forms.CharField(label='Car Make')
	model = forms.CharField(label='Model', max_length=15)
	year = forms.IntegerField(label='Year', max_value=2015)
