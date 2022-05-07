from . import views
from django.urls import path , include
urlpatterns = [
    path(r'login/',views.login),
    path(r'logout/',views.logout),
    path(r'register/',views.register),
    path(r'showprofile/',views.show_profile),
    path(r'home/',views.show_home),
    path(r'save_user/',views.save_user),
    path(r'edit_profile/',views.edit_prifile),
]
