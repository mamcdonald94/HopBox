from django.shortcuts import render, redirect
from .models import User, Product, Review, UserImage, Subscription


# Create your views here.
def disp_home(request):

    print("Displaying Home page")

    if 'user_id' in request.session:

        print("Displaying Home page for logged in user")   

        context = {}

        return render(request, "home.html",context)

    else:
        context = {
            "login_msg" : "Please log in first."
        }

        return render(request, "login.html", context) 



def disp_cart(request):

    print("Displaying Cart page")  

    if 'user_id' in request.session:

        print("Displaying Cart page for logged in user")  

        context = {}

        return render(request, "cart.html",context)

    else:
        context = {
            "login_msg" : "Please log in first."
        }

        return render(request, "login.html", context) 





def  disp_option(request,optionNum):  

    print("Displaying Option page")  

    if 'user_id' in request.session:

        print("Displaying Option page for logged in user")  
        print(optionNum)
        context = {}

        return render(request, "option.html",context)

    else:
        context = {
            "login_msg" : "Please log in first."
        }

        return render(request, "login.html", context) 

