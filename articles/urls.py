from django.urls import path
from . import views

urlpatterns = [
    path('articles-list',views.articles_list_view,name='articles-list'),
    path('categories',views.category_list_view,name='categories'),
    path('category-post/<int:id>',views.category_post_view,name='category-post'),
    path('user-articles',views.user_article_list_views,name='user-articles'),
    path('article_details/<int:id>',views.article_details_view,name='article-details'),
    path('update_details/<int:id>',views.article_update_view,name='update-details'),
    path('create-article',views.article_create_view,name='create-article'),
    path('delete-article/<int:id>',views.article_delete_view,name='delete-article'),
]