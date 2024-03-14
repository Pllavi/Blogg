"""
URL configuration for Blogs project.

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
from django.conf.urls.static import static
from django.conf import settings
from myblog import views


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('myblog.urls')),
path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('dashboard/', views.HomePage, name='dashboard'),
path('blog/', views.blog, name='blog'),
path('subscription/', views.subscription_page, name='subscription_page'),
                  # path('login/', views.CustomLoginView.as_view(), name='login'),
                  path('logout/', views.CustomLogoutView.as_view(), name='logout'),
path('create/', views.create_blog_post, name='create_blog_post'),
                  path('edit/<int:category_id>/<int:post_id>/', views.edit, name='edit'),



    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)