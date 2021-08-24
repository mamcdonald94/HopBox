from django.shortcuts import render, redirect
from .models import User, Product, Review, UserImage, Subscription
from .forms import *
from django.contrib import messages
import bcrypt


def landing_page(request):
    return render(request, 'index.html')

def disp_home(request):

    if 'user_id' in request.session:

        user_obj = User.objects.get(id=request.session['user_id'])
        subscript_objs = Subscription.objects.all()

        context = {
            'user' : user_obj,
            'subscriptions' : subscript_objs,
        }

        return render(request, "home.html",context)

    else:
        context = {
            "login_msg": "Please log in first."
        }

        return render(request, "login.html", context) 



def disp_cart(request):

    print("Displaying Cart page")  

    if 'user_id' in request.session:
        if request.method == "POST":
            print("Displaying Cart page for logged in user")  

            user_obj = User.objects.get(id=request.session['user_id'])
            subscript_obj = Subscription.objects.get(id=request.post['sel_subscription'])

            context = {
                'user' : user_obj,
                'subscriptions' : subscript_obj,
            }

            return render(request, "cart.html",context)
        else:
            redirect("home")
    else:
        context = {
            "login_msg" : "Please log in first."
        }

        return render(request, "login.html", context) 


def submit_order(request):
    print("Order placed!")

    return redirect("/cart")


def  disp_option(request,optionNum):  

    print("Displaying Option page")  

    if 'user_id' in request.session:

        print("Displaying Option page for logged in user")  

        user_obj = User.objects.get(id=request.session['user_id'])
        subscript_obj = Subscription.objects.get(option_id = optionNum)
        review_objs = Review.objects.filter(review_of = subscript_obj)
        userimage_objs = UserImage.objects.filter(image_for_review = review_objs)

        context = {
            'user' : user_obj,
            'subscriptions' : subscript_obj,
            'reviews' : review_objs,
            'user_images' : userimage_objs,
        }

        return render(request, "option.html", context)


    else:
        context = {
            "login_msg" : "Please log in first."
        }

        return render(request, "login.html", context) 


def add_review(request):

    print("Displaying Option page")  

    if 'user_id' in request.session:
        if request.method == "POST":
            print("Displaying Option page for logged in user") 

            optionNum = request.POST['optionNum']

            user_obj = User.objects.get(id=request.session['user_id'])
            subscript_obj = Subscription.objects.get(option_id = optionNum)

            Review.objects.create(
                comment = request.POST['comment'],
                submited_by = user_obj,
                review_of = subscript_obj,
                score = request.POST['score']
            )

        return redirect("/option" + str(optionNum))


    else:
        context = {
            "login_msg" : "Please log in first."
        }

        return render(request, "login.html", context) 



def add_user_image(request):

    print("Adding user image to option page")  

    if 'user_id' in request.session:

        if request.method == "POST":
            print("Adding user image to option page for logged in user")  

            optionNum = request.POST['optionNum']
            user_obj = User.objects.get(id=request.session['user_id'])
            subscript_obj = Subscription.objects.get(option_id = optionNum)
            review_objs = Review.objects.filter(review_of = subscript_obj)

            UserImage.objects.create(
                user_image_path = "",
                user_image_alt = "Uploaded image for Option " + str(optionNum),
                image_for_review = review_objs.last(),
                image_from_user = user_obj,
            )

        return redirect("/option" + str(optionNum))


    else:
        context = {
            "login_msg" : "Please log in first."
        }

        return render(request, "login.html", context) 

def registration(request):
    # creates a form
    form = RegistrationForm()
    context = {
        "RegForm": form,
    }
    return render(request, "register.html", context)

def create_user(request):
    if request.method == 'POST':
        # sends form data to backend for validation
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            # creates object but allows for further editing of object attributes (i.e., hashing the user password)
            new_user = reg_form.save(commit=False)
            hash_pw = bcrypt.hashpw(reg_form.cleaned_data['password'].encode(), bcrypt.gensalt()).decode()
            new_user.password = hash_pw
            new_user.save()
            # stores the logged in user's id for usage elsewhere in app
            request.session['user_id'] = new_user.id
            return redirect('/home')
        else:
            # if data does not pass validations, render form along with errors
            return render(request, 'register.html', context={'RegForm': reg_form})

def manage_account(request):
    if 'user_id' in request.session:
        this_user = User.objects.get(id=request.session['user_id'])
        account_form = EditAccountForm(instance=this_user)
        context = {
            'AccountForm': account_form,
            'this_user': this_user,
        }
        return render(request, 'edit_account.html', context)
    else:
        context = {
            "login_msg" : "Please log in first."
        }
        return render(request, "login.html", context) 

def update_account(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            this_user = User.objects.get(id=request.session['user_id'])
            account_form = EditAccountForm(request.POST, instance=this_user)
            if account_form.is_valid():
                # creates object but allows for further editing of object attributes (i.e., hashing the user password)
                edited_account = account_form.save(commit=False)
                hash_pw = bcrypt.hashpw(account_form.cleaned_data['password'].encode(), bcrypt.gensalt()).decode()
                edited_account.password = hash_pw
                edited_account.save()
                messages.success(request, 'you have successfully updated your account!')
                return redirect('/manage-account')
            
            return render(request, 'edit_account.html', context={'AccountForm': account_form})

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            # checks to see if the password submitted matches the password in the database
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                # holds the id of the currently logged in user, redirects to their dashboard
                request.session['user_id'] = logged_user.id
                return redirect('/home')

        messages.error(request, "invalid email or password")
    return redirect('/login')

def login_page(request):
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/')