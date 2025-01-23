from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.Home,name='HomePage'),
    path('register/',views.register,name='Register'),
    path('login/',views.Login,name='Login'),
    path('users/',views.users,name='Users'),
    path('addstudy/',views.AddStudy,name='AddStudy'),
    path("view/<id>/",views.View,name="View"),
    path("update/<id>/",views.Update,name="Update"),
    path('confirmdelete/<id>',views.ConfirmDelete,name="ConfirmDelete"),
    path('delete/<id>/',views.Delete,name="Delete"),
    path('logout/',views.Logout,name='Logout'),
]