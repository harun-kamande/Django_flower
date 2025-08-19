from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, Flower, Order
from .Hash_password import hash_password

# Create your views here.
def home(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

def add_cart(request):
    return render(request, 'cart.html' )

def profile(request):
    return render(request, 'profile.html')

def login(request):
    if request.mothod== "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        hashed_password=hash_password.hash_password(password)

        user=Users.objects.filter(email=email,password=hashed_password).first()
        if user:
            request.session['user_id'] = user.id
            return render(request, 'home.html', {'user': user})
        else:
            return HttpResponse("Invalid credentials")
        
    return render(request, 'login.html')
