from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#envio de datos a la vista
from .forms import ContactDataForm, ContactFormModelForm, UserRegisterForm
from .models import Flan,ContactForm

def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    return render(request,'index.html',{
    #aca va la lista de flanes, como clave valor
    'public_flans':public_flans
    })

@login_required
def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request,'welcome.html',{
        'private_flans': private_flans
    })

def about(request):
    flans = Flan.objects.filter()
    return render(request,'about.html',{
    #aca va la lista de flanes, como clave valor
    'flans':flans
    })

def contacto(request):
    if request.method == 'POST':
        #form = ContactDataForm(request.POST)
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            #se crea un objeto contactform con los datos recolectados
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        #form = ContactDataForm()
        form = ContactFormModelForm()
    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html',{})

def colaboradores(request):
    return render(request, 'colaboradores.html',{})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return HttpResponseRedirect('/exito_registro')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html',{ 'form': form })

def exito_registro(request):
    return render(request, 'exito_registro.html',{})