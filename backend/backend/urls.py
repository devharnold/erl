"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mod.views import ArticleList, ArticleDetail, BlogList, BlogDetail, PostList, PostDetail, SearchUserView
from django.conf import settings
from django.conf.urls.static import static
from mod.views import LoginView, UserSignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search-users/', SearchUserView.as_view(), name='search_users'),
    #path('', include('article.urls')),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('blogs/', BlogList.as_view(), name='article-list'),
    path('blogs<int:pk>/', BlogDetail.as_view(), name='blog-list'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)