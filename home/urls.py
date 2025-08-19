from django.urls import path,include
from .views import add_cart,login,profile,home,about,create

urlpatterns=[
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('add_cart/', add_cart, name='add_cart'),
    path("",home,name="default_page"),
    path("login/", login, name="login"),
    path("create/", create, name="create")


]   
