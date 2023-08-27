from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Details
from django.core.mail import send_mail
from django.contrib.auth import get_user
from .models import UserProfile
import datetime


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        p1 = request.POST['p1']
        p2 = request.POST['p2']
        if p1 == p2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "A User With This Email Already Exist Please Try Another")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "A User With This Username/Nickname Already Exist Please Try Another")
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, password=p1, username=username)
                user.save()
                obj = Details(username=username)
                obj.save()
                subject = "GhostTalker"
                msg = "Email have been confirmed successfully!!"
                to = email
                res = send_mail(subject, msg, "oniyidefaith30@gmail.com", [to])
                if res == 1:
                    return redirect('/')
                else:
                    messages.info(request, "Something went wrong")
                    return redirect('register')
        else:
            messages.info(request, "Password doesn't match try again")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('un', '')
        pass1 = request.POST.get('pa', '')
        user = auth.authenticate(username=uname, password=pass1)
        if user is None:
            messages.info(request, "invalid username/password")
            return redirect('login')
        else:
            auth.login(request, user)
            request.session['user_id'] = user.id  # Store the user's id in the session
            return redirect("link")

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("login")


def link_view(request):
    unique_id = request.GET.get('id')  # Extract the unique identifier from the URL parameters
    return render(request, 'link.html', {'unique_id': unique_id})


def room_view(request, room_name):
    unique_id = request.GET.get('id')  # Extract the unique identifier from the URL parameters
    user_id = request.session.get('user_id')

    # Retrieve the user object using the stored user ID
    user = get_user(request)

    return render(request, 'chatPage.html',
                  {'room_name': room_name, 'user_id': user_id, 'unique_id': unique_id, 'user': user})
