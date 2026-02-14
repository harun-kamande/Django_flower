from django.urls import path,include
from .views import add_cart,login,profile,home,about,create,shop,cart,check_out,land_page

urlpatterns=[
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('add_cart/', add_cart, name='add_cart'),
    path("",land_page,name="default_page"),
    path("login/", login, name="login"),
    path("create/", create, name="create"),
    path("shop/", shop, name="shop"),
    path("cart/", cart, name="cart"),
    path("profile/", profile, name="profile"),
    path("check_out/",check_out, name="check_out"),
    path("landing_page/",land_page, name="land_page")


]   
