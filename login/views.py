from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from mysite import settings
from .models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes ,force_str
from .token import generate_token


def home(request):
    return render(request,'login/index.html')


def validate_signup_form(username, fullname, email, password, password_confirm, request):
    """
    Validates the signup form inputs
    """
    if User.objects.filter(username=username).exists():
        messages.error(request, "Username already exists, please choose another.")
        return False

    if User.objects.filter(email=email).exists():
        messages.error(request, "Email is already registered!")
        return False

    if password != password_confirm:
        messages.error(request, "Passwords do not match.")
        return False

    if not username.isalnum():
        messages.error(request, "Username must be alphanumeric.")
        return False

    return True


def create_user(username, fullname, email, password):
    """
    Creates and returns a new user, or None if unsuccessful
    """
    try:
        user = User(username=username, fullname=fullname, email=email)
        user.set_password(password)  # Use Django's set_password for hashing
        user.is_active = False  # User will activate after email confirmation
        user.save()
        return user
    except Exception as e:
        print(f"Error creating user: {e}")
        return None


def send_welcome_email(user):
    """
    Sends a welcome email to the user
    """
    subject = "Welcome to ConnectionHelp!"
    message = (
        f"Hello {user.fullname}!\n"
        "Welcome to ConnectionHelp!\n"
        "Thank you for joining us. Please confirm your email to activate your account.\n"
        "Thank you,\nConnectionHelp Team"
    )
    from_email = settings.EMAIL_HOST_USER
    to_list = [user.email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)


def send_confirmation_email(user, request):
    """
    Sends a confirmation email to the user
    """
    current_site = get_current_site(request)
    email_subject = "Confirm your email @ ConnectionHelp!"
    message = render_to_string('login/email_confirmation.html', {
        'name': user.fullname,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user),
    })

    email = EmailMessage(
        email_subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
    )
    email.fail_silently = True
    email.send()


def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('volnteer_charity')

        else:
            messages.error(request,"Somthing not match")
            return redirect('/')

    return render(request, 'login/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfuly!")
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if (user is not None and generate_token.check_token(user, token)):
        user.is_active = True
        user.save()
        #login(request, user)
        return redirect('/')
    else:
        return render(request, 'login/activation_failed.html')

def signup(request):
    # Get form data
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password_confirm = request.POST.get('pass2', '').strip()
        # Validate form data
        if not validate_signup_form(username, fullname, email, password, password_confirm, request):
            return redirect('signup')
        # Create and save user
        user = create_user(username, fullname, email, password)
        if not user:
            return redirect('signup')
        # Send confirmation and welcome emails
        send_welcome_email(user)
        send_confirmation_email(user, request)
        messages.success(request, "Your account has been created successfully! Please confirm your email to activate your account.")
        return redirect('signin')
    return render(request, 'login/signup.html')
