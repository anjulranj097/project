from django.urls import path
from . import views

urlpatterns = [
    path('',views.fn_page),
    path('userlogin/',views.fn_userlogin),
    path('userregister/',views.fn_Userregister),
    path('changepass/',views.fn_ChangePassword),
    path('viewprofile/',views.fn_ViewProfile),
    path('addfriend/',views.fn_AddFriend)
]