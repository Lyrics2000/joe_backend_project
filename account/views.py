from django.shortcuts import redirect, render
from .forms import SignINForm,SignUpForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from account.models import User
from django.contrib.auth import logout
from .forms import UploadImageForm
from .models import User
from .models import Profile_pic
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import ASCTIME_DATE, urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token,password_reset_token
from django.core.mail import EmailMessage
from django.http import HttpResponse

from drugs.models import Notifications
from mainapp.models import AllBroadcast
from .models import Codes

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect("/")

def index(request):

    login_form = SignINForm(request.POST,None)

    context = {
        'login' : login_form
    }
    
    if login_form.is_valid:
        username = request.POST.get("email")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request,username = username, password = password )
        if user is not None:
            login(request,user)
            print("user....")
            return redirect("account:two_factor")
        else:
            pass
    return render(request,'signin.html',context)

@login_required(login_url="account:sign_in")
def two_factor(request):
    user_id =  request.user.id
    user_obj = User.objects.get(id = user_id)
    code = Codes.objects.get(user =  user_obj)

    if request.method == "POST":
        code_req  = request.POST.get("codes")
        if(int(code_req) == int(code.number)):
            return redirect("mainapp:index")
        else:
            return redirect("account:two_factor")

    context = {
        'codes':code
    }

    return render(request,'two_factor.html',context)


def signup(request):
    sign_up = SignUpForm(request.POST,None)

    context =  { 
        "form" :sign_up
    }
    if request.method =='POST':
        if sign_up.is_valid:
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name =  request.POST.get("last_name")
   
            phone =  request.POST.get("phone")
            email = request.POST.get('email')
            password = request.POST.get("password")
            user = authenticate(request,username = email, password = password )
            if user is not None:
                print("user exists")
                return redirect("account:sign_in")
            else:
                
                user = User.objects.create_user(username = username , email = email , password = password)
                user.last_name = last_name
                user.first_name = first_name
                user.phone = phone
                user.is_active =  False
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate Your Account'
                message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMessage(email_subject, message, to=[to_email])
                email.send()
                return HttpResponse('We have sent you an email, please confirm your email address to complete registration')

    return render(request,'signup.html',context)


def profile_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            image =  request.FILES["image"]
            if request.user.is_authenticated:
                user =  request.user.id
                user_obj =  User.objects.get(id=  user)
                obj,created =  Profile_pic.objects.get_or_create(user_id = user_obj)
                obj.image = image
                obj.save()

                return redirect("/")


            else:
                return redirect("accounts:sign_in")
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form' : form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user)
        current_site = get_current_site(request)
        email_subject = 'Successfull Registration'
        message = render_to_string('successfull_regestration.html', {
        'user': user,
        'domain': current_site.domain
        })
        to_email = user.email
        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()

        return HttpResponse('Your account has been activate successfully')
        
    else:
        return HttpResponse('Activation link is invalid!')




def profile_account(request):
    user_id =  request.user.id
    user_obj =  User.objects.get(id = user_id)
    personalize_not =  Notifications.objects.filter(user_id =  user_obj)
    all_messages =  AllBroadcast.objects.all()
    context = {
        'just_for_you' :  personalize_not,
        'all_messages' :  all_messages
    }

    return render(request,'profile.html',context)



def password_reset(request):
    msg = ''
    if request.method == "POST":
        email = request.POST.get('email')
        qs = User.objects.filter(email=email)
        site = get_current_site(request)

        if len(qs) > 0:
                user = qs[0]
                user.is_active = False  # User needs to be inactive for the reset password duration
                user.reset_password = True
                user.save()
                

                email_subject = 'Reset Password'
                message = render_to_string('reset_password_email.html', {
                    'user': user,
                    'protocol': 'http',
                    'domain': site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = user.email
                email = EmailMessage(email_subject, message, to=[to_email])
                email.send()

                return HttpResponse('Reset Password Email Sent Successfully')

    
    return render(request,'user_forget_pass.html')



def reset(request,uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        request.session['user_id'] =  user.id
        return render(request,'password_reset.html')        
    else:
        return HttpResponse('Activation link is invalid!')



def change_user(request):
    user_id =  request.session.get("user_id")
    if request.method == "POST":
        passs =  request.POST.get("password")
        print(passs)
        user_obj =  User.objects.get(id = user_id)
        user_obj.set_password(passs)
        user_obj.save()
        
        del request.session['user_id']
        return redirect("account:sign_in")

            


    

    