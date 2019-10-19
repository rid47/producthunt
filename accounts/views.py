from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        # USER WANT TO SIGN UP
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.get(username = request.POST['username'])
                print(f"User: {user}")
                return render(request,'accounts/signup.html',{'error': 'User name already taken!'})
            else:
                return render(request, 'accounts/signup.html', {'error': 'Password must match!'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'],'',request.POST['password1'])
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request,'accounts/signup.html')



def login(request):
    return render(request,'accounts/login.html')


def logout(request):
    return render(request,'accounts/signup.html')
