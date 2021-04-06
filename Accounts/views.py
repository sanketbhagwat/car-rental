from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def account(request):
    return render(request,'account.html')
def login(request):
    redirect_to = request.GET.get('next', '')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            # request.session['customer']=user
            if 'next' in request.POST:
                request.session['customer_id']=user.id
                return redirect(request.POST.get('next'))
                
            else:
                if redirect_to:
                    request.session['customer_id']=user.id
                    return HttpResponseRedirect(redirect_to)
                else:
                    request.session['customer_id']=user.id
                    return redirect('/')

        else:
            messages.error(request,'invalid credit')
            return redirect('login')
    else:
        return render(request,'users/login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.


def register(request):
    # form=UserCreationForm()
    # context={
        #   "form":form
    # }
    if request.method =='POST':
        first_name=request.POST['firstname']
        email=request.POST['email']
        password=request.POST['pass1']
        user_name=request.POST['username']
        if User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('register')
        else:
            user=User.objects.create_user(username=user_name,password=password,first_name=first_name,email=email)
            user.save();
            return redirect('login')
    else:
        return render(request,'users/register.html')

   



















