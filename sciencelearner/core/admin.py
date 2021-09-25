from django.contrib import admin
from .models import ContactModelForm, ProfileModel, JoinModelForm, YourCommentModelForm, EnrolledCoursedModelForm, FacultymembersDetail
from django.contrib.auth.models import User

# Register your models here.

@admin.register(ContactModelForm)
class AdminContactForm(admin.ModelAdmin):
  list_display=['fullname','email','phone','msg']

@admin.register(ProfileModel)
class AdminProfileForm(admin.ModelAdmin):
  list_display=['myid','username','firstname','lastname','profile']

@admin.register(JoinModelForm)
class AdminProfileForm(admin.ModelAdmin):
  list_display=['firstname','lastname','stdortea','email','contactno']

@admin.register(YourCommentModelForm)
class yourcommentadminform(admin.ModelAdmin):
  list_display=['myid','username','name','firstletterofname','comment']

@admin.register(EnrolledCoursedModelForm)
class EnrolledCourseAdminForm(admin.ModelAdmin):
  list_display=['myid','username','stdfullname','stdemail','contactno','onlineoroffline','neet','jee','class12','class11','class12','class11crashcourse','class12crashcourse','class6to10']
  
  
@admin.register(FacultymembersDetail)
class FacultymembersDetailAdminForm(admin.ModelAdmin):
  list_display=['id','fmname','fmqualification','fmspecility','fmwords']
  

