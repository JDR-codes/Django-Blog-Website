from django.urls import path
from . import views

urlpatterns = [
    path('user-create',views.user_create,name='user_create'),
    path('profile/<str:user>',views.view_profile,name='profile'),
    path('update-profile/<int:id>',views.edit_profile,name='update-profile'),
    path('follow/<int:id>',views.follow_user_view,name='follow')
]