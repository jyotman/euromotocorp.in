from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import NameForm

def home(request):
    redirect = request.GET.get('redirect')
    if redirect :
        return render(request, 'wheels/mdl/templates/main/index.html', {"redirect" : True})
    return render(request, 'wheels/mdl/templates/main/index.html', {})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	choice = form.cleaned_data['choice']
        	name = form.cleaned_data['name']
        	mobile = form.cleaned_data['mobile']
        	car_make = form.cleaned_data['car_make']
        	model = form.cleaned_data['model']
        	year = form.cleaned_data['year']

        	recipients = ['jyotman94@gmail.com', 'euromotocorp@gmail.com']

        	msg = 'Category : ' + choice + '\n\nName : ' + name + '\n\nMobile : ' + str(mobile) + '\n\nCar Make : ' + car_make + '\n\nModel : ' + model + '\n\nYear : ' + str(year)

        	send_mail('Test Message', msg, 'euromotocorp@gmail.com', recipients)

        	return HttpResponseRedirect('/?redirect=true')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'wheels/name.html', {'form': form.as_p()})

def repairTyre(request):
    return render(request, 'wheels/tyre.html')

def repairAlloy(request):
    return render(request, 'wheels/alloy.html')