from django.urls import path
from . import views

urlpatterns = [
    path('add-comment/<int:id>',views.add_comment_view,name='add-comment'),
    path('delete-comment/<int:id>',views.delete_comment_view,name='delete-comment'),
    path('like/<int:id>',views.like_article_view,name='like')
]