from django.urls import path 
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('profile/', views.profile, name="profile"),
    path('signout/', views.signout, name="signout"),
    path('contact/', views.contact, name="contact"),
    path('joinus/', views.jointheinst, name="joinus"),
    path('choosecourse/', views.selectcourses, name="choosecourse"),
    path('update/<int:pk>/', views.UpdateUserData.as_view(template_name="core/updateprofile.html"), name="updateprofile"),
    path('deleteaccount/', views.deleteaccount, name="deleteacc"),
    path('deleteaccountSuperuser/<slug:usr>/', views.deleteaccountSuper, name="deleteSupUsr"),
    path('viewallcomments/', views.viewallcomments, name="viewallcomments"),
]
