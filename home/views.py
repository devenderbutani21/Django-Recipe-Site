from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     'variable' : 'this is variable' 
    # }
    # messages.success(request, 'Your profile was updated.')
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')

def recipes(request):
    return render(request, 'recipes.html')

def contact(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email, phone=phone, date=datetime.today())
        contact.save()
        messages.success(request, str('Your details have been submitted!'))
    return render(request, 'contact.html')