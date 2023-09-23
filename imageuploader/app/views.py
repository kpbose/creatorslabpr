from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from .forms import *
# Create your views here.
def signup(request):
    if request.method=="POST":
          username=request.POST['username']
          first=request.POST['first']
          last=request.POST['last']
          password=request.POST['password']
          confirm=request.POST['con_password']
          email=request.POST['email']
          users=User.objects.all()
          j=0
          for i in users:
               if username in i.username:
                   j+=1
          if password==confirm and j==0:
              myuser=User.objects.create_user(username=username,email=email,password=password)
              myuser.first_name=first
              myuser.last_name=last
              myuser.save()
              return render(request,"signin.html",{'msg':'Registered succesfully'})
          else:
               return render(request,"signup.html",{'error':'passwords not matching or username already exist'})
    return render(request,"signup.html")
def signin(request):
    error_message=''
    if request.method=='POST':
        error_message='Invalid Credentials'
        username=request.POST['username']
        password=request.POST['password']
        existing=User.objects.all()
        for users in existing:
            if(str(users)==str(username)):
                  valid_user= authenticate(username=username,password=password)  
                  if valid_user is not None:
                    login(request,valid_user)
                    fname=valid_user.first_name
                    form = FileUploadForm()
                    allfile=UploadedFile.objects.filter(user=request.user)

                    return render(request,"home.html",{'fname':fname,'form':form,'allfile':allfile})
    return render(request,'signin.html',{'error_message':error_message})
def home(request):
    allfile=UploadedFile.objects.filter(user=request.user)
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            allfile=UploadedFile.objects.filter(user=request.user)
            print(allfile)
            return render(request,'home.html',{'status':' Upload Successful','allfile':allfile})
        else:
            return render(request,'home.html',{'status':'Form is not valid','allfile':allfile})

    else:
        form = FileUploadForm()
    return render(request, 'home.html', {'form': form,'allfile':allfile})