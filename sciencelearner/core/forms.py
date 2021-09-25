from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from .models import ContactModelForm, ProfileModel, JoinModelForm, YourCommentModelForm, EnrolledCoursedModelForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class StudentLoginForm(AuthenticationForm):
  username=UsernameField(widget=forms.TextInput(attrs=
  {'autofocus':True, 'class':'form-control','placeholder':'Enter Username'}))
  
  password=forms.CharField(label=_("Password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
  'class':'form-control','placeholder':'Enter Password'}))

class StudentSignupForm(UserCreationForm):
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}), label="Password")
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}), label="Confirm Password")
  
  class Meta:
    model=User
    fields=['username','first_name','last_name','email']
    widgets={'username':forms.TextInput(attrs={'class':'form-control',
              'placeholder':'Enter Username'}),
              'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
              'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
              'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'})}
              
class ProfileForm(forms.ModelForm):
  class Meta:
    model = ProfileModel
    fields = ['profile']
              

class ContactForm(forms.ModelForm):
  phone = PhoneNumberField(
    widget=PhoneNumberPrefixWidget(initial='IN', attrs={'class':'form-control','placeholder':'Enter Contact No.'})
  )
  class Meta:
    model = ContactModelForm
    fields=['fullname','email','phone','msg']
    
    labels = {'fullname':'Full Name', 'email':'Email', 'phone':'Phone', 'msg':'Message'}
    
    widgets={'fullname':forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Full Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'msg':forms.Textarea(attrs={'class':'form-control','placeholder':'Your Message','cols':20, 'rows':5}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone No.'})}
            
class JoinForm(forms.ModelForm):
  contactno=PhoneNumberField(
    widget=PhoneNumberPrefixWidget(initial="IN", attrs={'class':'form-control','placeholder':'Enter Contact No.'})
  )
  class Meta:
    model = JoinModelForm
    fields = "__all__"
    labels = {'firstname':'First Name', 'lastname':'Last Name', 'email':'Email', 'stdortea':'Want To Join As','contactno':'Contact No.'}
    
    widgets={'firstname':forms.TextInput(attrs={'class':'form-control',
              'placeholder':'Enter First Name'}), 
              'lastname':forms.TextInput(attrs={'class':'forn-control', 'placeholder':'Enter Last Name'}),
              'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}), 
              'contactno':forms.NumberInput(attrs={'class':'form-control','placeholer':'Enter Contact No.'})}
              


class YourCommentForm(forms.ModelForm):
  class Meta:
    model = YourCommentModelForm
    fields=['name','comment']
    widgets={'name':forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Enter Your Name'}),
            'comment':forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'})}

class EnrolledCoursedForm(forms.ModelForm):
  contactno=PhoneNumberField(
    widget=PhoneNumberPrefixWidget(initial='IN', attrs={'class':'form-control','placeholder':'Enter Contact no.'})
  )
  class Meta:
    model = EnrolledCoursedModelForm
    fields=['stdfullname','stdemail','contactno','onlineoroffline','neet','jee','class11','class12','class11crashcourse','class12crashcourse','class6to10']
    labels = {'stdfullname':'Student Full Name','stdemail':'Email','contactno':'Phone No','onlineoroffline':'Choose Mode'}
    widgets={'stdfullname':forms.TextInput(attrs={'class':'form-control',
              'placeholder':'Enter full Name'}), 
              'stdemail':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}), 
              'contactno':forms.NumberInput(attrs={'class':'form-control','placeholer':'Enter Contact No.'})}
