from django.shortcuts import render,redirect
import json
from django.http import HttpResponse,JsonResponse
from .models import Users, Flower, Order,OrderItem
from .hash_password import hash_password
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_cart(request):
    return render(request, 'cart.html' )

def profile(request):
    user_id = request.session.get("user_id")
    if not user_id:
        # No user logged in
        return render(request, "profile.html", {"user": None, "orders": []})

    try:
        user = Users.objects.get(id=user_id)
        orders = user.orders.prefetch_related("items__flower").order_by("-date_ordered")
    except Users.DoesNotExist:
        # User not found in database
        return render(request, "profile.html", {"user": None, "orders": []})

    return render(request, "profile.html", {"user": user, "orders": orders})


def login(request):
    # if request.mothod== "POST":
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')
    #     hashed_password=hash_password.hash_password(password)

    #     user=Users.objects.filter(email=email,password=hashed_password).first()
    #     if user:
    #         request.session['user_id'] = user.id
    #         return render(request, 'home.html', {'user': user})
    #     else:
    #         return HttpResponse("Invalid credentials")
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hash_password(password)

        user = Users.objects.filter(email=email, password=hashed_password).first()

        if user:
            request.session['user_id'] = user.id
            return render(request, 'home.html', {'user': user})
        else:
            return HttpResponse("Invalid credentials")


def create(request):
    if request.method == "GET":
        return render(request, 'create_account.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        profile_photo = request.FILES.get('profile_photo')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = hash_password(password)

        # check if user exist in the database

        user=Users.objects.filter(email=email).first()

        if user:
            message = "User already exists"
            messages.error(request, message)
            return render(request, 'create_account.html', {"error": message})
        else:
            user = Users(email=email, password=hashed_password, username=username, profile_photo=profile_photo)
            user.save()
            return render(request, 'login.html')
    return render(request, 'create_account.html')

def shop(request):
    flowers = Flower.objects.all()
    return render(request, 'shop.html', {'flowers': flowers})

def cart(request):
    return render(request, 'cart.html')

def check_out(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            cart = data.get("cart", [])
            address = data.get("address", "No address provided")

            if not cart:
                return JsonResponse({"success": False, "error": "Cart is empty"})

            # Get logged-in user
            user_id = request.session.get("user_id")
            if not user_id:
                return JsonResponse({"success": False, "error": "User not logged in"})
            
            user = Users.objects.get(id=user_id)

            # Create new order linked to user
            order = Order.objects.create(
                user=user,
                delivery_address=address
            )

            # Add items
            for item in cart:
                flower = Flower.objects.get(name=item["name"])
                OrderItem.objects.create(
                    order=order,
                    flower=flower,
                    quantity=item["quantity"]
                )
                flower.remainig -= int(item["quantity"])
                flower.save()

            return JsonResponse({"success": True, "order_id": order.id})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return render(request, "check_out.html")
