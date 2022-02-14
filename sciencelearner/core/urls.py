from django.urls import path 
from . import views

from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('profile/', views.profile, name="profile"),
    path('signout/', views.signout, name="signout"),
    path('contact/', views.contact, name="contact"),
    path('joinus/', views.jointheinst, name="joinus"),
    path('choosecourse/', views.selectcourses, name="choosecourse"),
    path('coursedetails/', views.coursedetails, name="coursedetails"),
    path('update/<int:pk>/', views.UpdateUserData.as_view(template_name="core/updateprofile.html"), name="updateprofile"),
    path('deleteaccount/', views.deleteaccount, name="deleteacc"),
    path('deleteaccountSuperuser/<slug:usr>/', views.deleteaccountSuper, name="deleteSupUsr"),
    path('viewallcomments/', views.viewallcomments, name="viewallcomments"),
    path('addusersuper/', views.addusersuperuser, name="add-user-superuser"),
    path('changepassword/', views.changepassword, name="changepassword"),

    path('password_reset/', auth_view.PasswordResetView.as_view(template_name="core/registration/password_reset_form.html"), name="password_reset"),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name="core/registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="core/registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name="core/registration/password_reset_confirm.html"), name="password_reset_complete"),
]
