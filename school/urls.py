"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', blog_views.home, name='blog-home'),
    path('students/', blog_views.students, name='blog-students'),
    path('delete/<int:delete_id>', blog_views.delete, name='blog-delete'),
    path('edit/<int:edit_id>', blog_views.edit, name='blog-edit'),
    path('search/<int:search_id>', blog_views.search, name='blog-search'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='blog-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='blog-logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
