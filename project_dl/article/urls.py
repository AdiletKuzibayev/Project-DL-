from django.urls import path, include, re_path
import article.views
urlpatterns = [
    path('articles/all/', article.views.articles),
    path('articles/get/<int:article_id>/', article.views.article),
    path('articles/addlike/<int:article_id>/', article.views.addlike),
    path('search/', article.views.search, name='search'),
    path('articles/addcomment/<int:article_id>/', article.views.addcomment),
    path('page/<int:page_number>/', article.views.articles),
    path('', article.views.articles),
]