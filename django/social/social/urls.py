"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('',
    
     Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage,name="login"),
    path("homepage",views.homepage,name="homepage"),
    path('forgotpassword',views.forgot_password,name="forgotpassword"),
    path("passwordnew/<str:toke>",views.password_enter_new,name="newpassword"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('logout',views.logoutbutton,name="logout"),
    path('uploadpost',views.uploadpost,name="uploadpost"),
    path('signup',views.signup,name="signup")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)