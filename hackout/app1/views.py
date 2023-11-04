# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def LandingPage(request):
    return render(request, 'landing.html')

def InputPage(request):
    return render(request, 'input.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@login_required(login_url='login')
def generate_packing_list_api(request):
    if request.method == "POST":
        destination = request.POST.get('destination')
        season = request.POST.get('season')
        withKids = request.POST.get('withKids')
        seniorCitizens = request.POST.get('seniorCitizens')
        typeOfTravel = request.POST.get('typeOfTravel')
        modeOfTravel = request.POST.get('modeOfTravel')
        activities = request.POST.get('activities')
        
        # Check if destination is None
        if destination is None:
            return HttpResponse("Destination not provided in POST request")
        
        print("Destination:", destination)  # This should print to your server console
        
        return redirect('list')
    else:
        return render(request, 'input.html')




@login_required(login_url='login')
def list(request):
    packing_list = request.session.get('packing_list', [])
    return render(request, 'list.html', {'my_list': packing_list})

@login_required(login_url='login')
def download_list_pdf(request):
    packing_list = request.session.get('packing_list', [])
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="PackingList.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    for i, item in enumerate(packing_list, start=1):
        p.drawString(100, height - 100 - i * 14, f"{i}. {item}")

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
