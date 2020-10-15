from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

def contact(request):
    #print("tipo de petición: {}", request.method)
    #en el primero realizamos la instancia para que se cree el formulario
    contactform = ContactForm()
    #consultamos que si hay un envio entonces que tome los valores del formulario
    if request.method == "POST":
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo antes de redireccionar
            email = EmailMessage(
                "La caffetiera",
                "De {} <{}>\n\n{}".format(name, email, content),
                "no contestar",
                ["jetapia@itsgg.edu.ec"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #Si algo no va bien, ponemos el redirect
                return redirect(reverse('contact')+"?fail")
    return render(request, 'contact/contact.html', {'form': contactform})