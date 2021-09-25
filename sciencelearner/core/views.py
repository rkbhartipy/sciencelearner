from django.forms.utils import pretty_name
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentLoginForm, StudentSignupForm, ContactForm, ProfileForm, JoinForm, YourCommentForm, EnrolledCoursedForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import ProfileModel, YourCommentModelForm, EnrolledCoursedModelForm
from django.views.generic.edit import UpdateView
import random
from django.contrib.auth.decorators import login_required

# Create your views here.

# home and comments
def home(request):
  comment=YourCommentModelForm.objects.order_by('myid').reverse()[0:5]
  if request.method=="POST":
    if request.user.is_authenticated:
      formcmt=YourCommentForm(request.POST)
      if formcmt.is_valid():
        uid=request.user.id 
        uname=request.user.username
        namecmt=formcmt.cleaned_data['name']
        commentt=formcmt.cleaned_data['comment']
        firstletter=(namecmt[0]).upper()
        reg=YourCommentModelForm(username=uname, name=namecmt, comment=commentt, firstletterofname=firstletter)
        reg.save()
    else:
      formcmt=YourCommentForm()
      return render(request, "core/home.html", {'form':formcmt,'comments':comment})
  else:
    formcmt=YourCommentForm()
  return render(request, "core/home.html", {'form':formcmt,'comments':comment})

def signup(request):
  if not request.user.is_authenticated:
    if request.method=="POST":
      form=StudentSignupForm(request.POST)
      if form.is_valid():
        form.save()
        uname=form.cleaned_data['username']
        fname=form.cleaned_data['first_name']
        lname=form.cleaned_data['last_name']
        email1=form.cleaned_data['email']
        randval=random.randint(0,10000000)

        reg=ProfileModel.objects.create(myid=randval,username=uname,
        firstname=fname, lastname=lname, email=email1, profile="none")
        reg.save()

        reg=EnrolledCoursedModelForm.objects.create(myid=randval,username=uname,
        stdfullname=(fname+lname), stdemail=email1, contactno="0000000000",
        onlineoroffline="none", neet=False, jee=False,
        class11=False,class12=False, class11crashcourse=False,
        class12crashcourse=False, class6to10=False)
        reg.save()

        return redirect('/core/signin/')
    else:
      form=StudentSignupForm()
    return render(request, "core/signupform.html", {'form':form})
  else:
    return redirect('/core/profile/')

def signin(request):
  if not request.user.is_authenticated:
    if request.method=="POST":
      form=StudentLoginForm(request.POST, data=request.POST)
      if form.is_valid():
        uname=form.cleaned_data["username"]
        upass=form.cleaned_data["password"]
        usr=authenticate(username=uname, password=upass)
        if usr is not None:
          login(request, usr)
          return redirect('/core/profile/')
      else:
        messages.error(request,"Enter Valid Username Or Password")
        return render(request, 'core/signinform.html', {'form':form})
    else:
      form=StudentLoginForm()
    return render(request, "core/signinform.html", {'form':form})
  else:
    return redirect('/core/profile/')

@login_required(login_url="/core/signin/")
def profile(request):
  usr=request.user
  uid=usr.id
  fname=usr.first_name 
  lname=usr.last_name
  email=usr.email 
  uname=usr.username

  reg=ProfileModel.objects.filter(username=uname).update(myid=uid, firstname=fname, lastname=lname, email=email)
  reg=EnrolledCoursedModelForm.objects.filter(username=uname).update(myid=uid)

  # user data for superuser
  
  if request.user.is_authenticated:
    if request.method == "POST":
      form=ProfileForm(request.POST, request.FILES)
      if form.is_valid():
        picname=form.cleaned_data['profile']
        reg=ProfileModel(myid=uid, username=uname, email=email, firstname=fname, lastname=lname, profile=picname)
        reg.save()

    else:
      form=ProfileForm()
    img=ProfileModel.objects.get(myid=uid)
    coursedlt=EnrolledCoursedModelForm.objects.get(myid=uid)

    # send data for
    if usr.is_superuser:
      print("you are a superuser")
      allusers=User.objects.all()
      context={'firstname':fname, 'lastname':lname, 'email':email, 'username':uname, 'form':form, 'img':img,'usercoursedtl':coursedlt, "users":allusers}
      return render(request, "core/profilepage.html", context)
    else:
      print("you are not a superuser")
      context={'firstname':fname, 'lastname':lname, 'email':email, 'username':uname, 'form':form, 'img':img,'usercoursedtl':coursedlt}
      return render(request, "core/profilepage.html", context)
  else:
    return redirect('/core/signin/')

def contact(request):
  if request.method=="POST":
    form=ContactForm(request.POST)
    if form.is_valid():
      phone=form.cleaned_data['phone']
      if len(str(phone))!=10:
        print("length of the phone is :", len(str(phone)))
        return HttpResponse("enter phone non of 10 digits")
      else:
        form.save()
  else:
    form=ContactForm()
  return render(request, "core/contact.html", {'form':form})

class UpdateUserData(UpdateView):
  model = User
  fields = ['first_name','last_name', 'email']
  success_url = '/core/profile/'
  
def jointheinst(request):
  if request.method=="POST":
    form=JoinForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form=JoinForm()
  return render(request, "core/joinus.html", {'form':form})

def viewallcomments(request):
  allcomments=YourCommentModelForm.objects.order_by('myid').reverse()
  if request.method=="POST":
    if request.user.is_authenticated:
      form=YourCommentForm(request.POST)
      if form.is_valid():
        form.save()
    else:
      return redirect('/core/signin/')
  else:
    form=YourCommentForm()
  return render(request, "core/allcomments.html", {'comments':allcomments,'form':form})

def selectcourses(request):
  if request.user.is_authenticated:
    if request.method=="POST":
      form=EnrolledCoursedForm(request.POST)
      if form.is_valid():
        uname=request.user.username
        uid=request.user.id
        fname=form.cleaned_data['stdfullname']
        semail=form.cleaned_data['stdemail']
        sphone=form.cleaned_data['contactno']
        onoroffline=form.cleaned_data['onlineoroffline']
        sneet=form.cleaned_data['neet']
        sjee=form.cleaned_data['jee']
        sclass11=form.cleaned_data['class11']
        sclass12=form.cleaned_data['class12']
        sclass11crashcourse=form.cleaned_data['class11crashcourse']
        sclass12crashcourse=form.cleaned_data['class11crashcourse']
        sclass6to10=form.cleaned_data['class6to10']

        print("-------------------------",uname, uid, fname, semail, sphone, onoroffline, sneet, sjee, sclass11, sclass12, sclass11crashcourse, sclass12crashcourse)

        res=EnrolledCoursedModelForm.objects.filter(username=uname).update(myid=uid, stdfullname=fname, stdemail=semail, contactno=sphone, onlineoroffline=onoroffline, neet=sneet, jee=sjee, class11=sclass11, class12=sclass12, class11crashcourse=sclass11crashcourse, class12crashcourse=sclass12crashcourse, class6to10=sclass6to10)
        messages.info(request, "You have successfully choosen the courses")
        return render(request, 'core/choosecourseform.html', {'form':form})
    else:
      form=EnrolledCoursedForm()
    return render(request, 'core/choosecourseform.html', {'form':form})
  else:
    return redirect('/core/signin/')


def signout(request):
  logout(request)
  return redirect('/core/signin/')

def deleteaccount(request):
  reg1=User(id=request.user.id)
  reg2=ProfileModel.objects.filter(username=request.user.username)
  reg3=EnrolledCoursedModelForm.objects.filter(username=request.user.username)
  reg1.delete()
  reg2.delete()
  reg3.delete()

  logout(request)
  return render(request, "core/home.html")

def deleteaccountSuper(request, usr=None):
  print("delete method is called")
  print("and value of pk is :", usr)
  reg1=User.objects.filter(username=usr)
  reg2=ProfileModel.objects.filter(username=usr)
  reg3=EnrolledCoursedModelForm.objects.filter(username=usr)
  reg1.delete()
  reg2.delete()
  reg3.delete()
  return redirect('/core/profile/')

