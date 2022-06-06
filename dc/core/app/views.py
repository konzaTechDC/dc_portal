from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

def landing_page(request):
    return render(request, 'app/index.html')

def contact(request):
    form =  ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message submitted successfully. Customer care team will reach out shortly!")
            return redirect('index')

    # context = {
    #     "title": "Contact",
    #     "form": form
    # }
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form':form})

