"""
URL configuration for socialmedia project.

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
from django.urls import include, path
import accounts.views as accounts_views
import messaging.views as messaging_views
from . import views as socialmedia_views

urlpatterns = [
    path("", socialmedia_views.index, name="index"),  # Root URL for the homepage
    path("messaging/", include("messaging.urls")),  # URLs for the messaging app
    path("admin/", admin.site.urls),  # Admin site
    path("register/", accounts_views.register, name='register'),  # Custom registration view
    path("accounts/", include('django.contrib.auth.urls')),  # Built-in auth URLs under 'accounts/'
]
