from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signup_user,name='signup'),
    path('logout',views.logout_user,name='logout'),
    path('',views.login_user,name='login'),
]