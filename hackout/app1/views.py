# app1/views.py

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
# Function to generate a packing list
def get_packing_list(request):
    # For simplicity, we are returning a static list here.
    # You can replace this with a call to an external API or some other logic.
    return ["Passport", "Tickets", "Clothes", "Charger", "Toiletries"]

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

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

def LogoutPage(request):
    logout(request)
    return redirect('login')

def generate_list(request):
    travel_items = get_packing_list(request)
    context = {'my_list': travel_items}
    return render(request, 'list.html', context)

def download_list_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    travel_items = get_packing_list(request)
    y = 750
    for item in travel_items:
        p.drawString(100, y, f"- {item}")
        y -= 30
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="PackingList.pdf"'
    return response

@csrf_exempt
def generate_packing_list_api(request):
    if request.method == 'POST':
        output = get_packing_list(request)
        return JsonResponse({'output': output})
    return JsonResponse({'error': 'Invalid request'}, status=400)
def my_view(request):
    # Call the function that interacts with OpenAI API.
    packing_list = get_packing_list()
    # Render the packing list to a template or return as HTTP response.
    return HttpResponse(packing_list)