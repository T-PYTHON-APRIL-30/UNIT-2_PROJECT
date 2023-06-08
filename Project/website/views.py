from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail,EmailMessage
from .models import inquiry,comment,novel


def index_page(request:HttpRequest):
    return render(request, "website/index.html")

def Submission(request:HttpRequest):
    return render(request, "website/Submission.html")

def not_ready(request:HttpRequest):
    return render(request, "website/not_ready.html")

def damn(request:HttpRequest):
    return render(request, "website/404.html")

def project_view(request:HttpRequest):
    try:
        return render(request,"website/prpject/html")
    except:
        return redirect("website:404")



def contact(request:HttpRequest):
    from dotenv import load_dotenv
    import os

    load_dotenv()  

    if request.method == "POST":
        if "file4" in request.FILES:
            file4 = request.FILES["file4"]  
            Inquiry = inquiry(fullname = request.POST["fullname"], emailAddress = request.POST["emailAddress"],type_of_inquery = request.POST["type_of_inquery"], message = request.POST["message"], file4 = file4)
            Inquiry.save()

            subject = 'New inquiry submitted'
            message = f'Full name: {request.POST["fullname"]}\nEmail address: {request.POST["emailAddress"]}\n Type: {request.POST["type_of_inquery"]}\nMessage: {request.POST["message"]}\nFile: {file4}'
            from_email = os.getenv("DEFAULT_FROM_EMAIL")

            recipient_list = [request.POST['emailAddress']]

            email = EmailMessage(
                subject,
                message,
                from_email,
                recipient_list,
                reply_to=[from_email],
            )

            email.attach(file4.name, file4.read() ,'application/pdf')
            email.send()
            return redirect("website:Submission")     
        else:
            
            
            Inquiry = inquiry(fullname = request.POST["fullname"], emailAddress = request.POST["emailAddress"],type_of_inquery = request.POST["type_of_inquery"], message = request.POST["message"])
            Inquiry.save()

            subject = 'New inquiry submitted'
            message = f'Full name: {request.POST["fullname"]}\nEmail address: {request.POST["emailAddress"]}\nType: {request.POST["type_of_inquery"]}\nMessage: {request.POST["message"]}'
            from_email = os.getenv("DEFAULT_FROM_EMAIL")

            recipient_list = [request.POST['emailAddress']]

            email = EmailMessage(
                subject,
                message,
                from_email,
                recipient_list,
                reply_to=[from_email],
            )
            email.send()
            return redirect("website:Submission")

        

   
def football_page(request:HttpRequest):
    return render(request, "website/football.html")

def writing_page(request:HttpRequest):
    novels = novel.objects.all()
    Comments = comment.objects.all()
    return render(request, "website/writing.html", {"novels":novels, "Comments":Comments})

def book(request:HttpRequest, novel_id):

    if request.method == "POST":
        novel1 = novel.objects.get(id = novel_id)
        Comment = comment(Novel = novel1, name = request.POST["name"], content = request.POST["content"])
        Comment.save()
        return redirect("website:details", novel_id = novel1.id)

    Novell = novel.objects.get(id = novel_id)
    Comments = comment.objects.filter(Novel= Novell)
    return render(request, "website/book.html", {"Novell":Novell, "Comments":Comments})

def software_page(request:HttpRequest):
    return render(request, "website/software.html")