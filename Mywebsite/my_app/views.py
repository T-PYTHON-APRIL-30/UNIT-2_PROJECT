from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from time import sleep

def home(request):
    return render(request,"my_app/home.html")




def contact(request):
        try:
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                message = request.POST.get('message')
                sub= request.POST.get('sub')

                # Save contact data to the database
                contact = Contact(name=name, email=email, message=message)
                contact.save()

                # Retrieve all contacts
                contacts = Contact.objects.all()
                print(contact.email,contact.name,contact.message,sub)
                # Send email
                send_mail(contact.name, contact.message,contact.email,['saudinfo004@gmail.com'])

                # Render success page or redirect
                return render(request, 'my_app/contact_success.html')

            return render(request, 'my_app/contact_list.html')
        except:
                return render(request,"my_app/about.html")





def about(request):
    return render(request,"my_app/about.html")


def work (requset):
    return render(requset,"my_app/work.html")


