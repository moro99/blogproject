"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import blog.views
import portfolio.views
import acounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #admin 경로
    path('home/', blog.views.home, name="home"), #home 경로
    path('blog/<int:blog_id>', blog.views.detail, name="detail"), #detail경로
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create/', blog.views.create, name="create"), #create함수 실행을 위한 경로
    path('portfolio/', portfolio.views.portfolio, name='portfolio'), #portfolio 경로
    path('signup/', acounts.views.signup, name='signup'),
    path('', acounts.views.login, name='login'),
    path('logout/', acounts.views.logout, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
