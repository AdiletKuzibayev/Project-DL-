"""project_dl URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
    path('', include('subjects.urls')),
=======
=======
>>>>>>> parent of 34c64c1... asd
    path('basicview/', include('article.urls')),
    path('auth/', include('loginsys.urls')),
    path('user/', include('subjects.urls')),
    path('mail/', include('mail.urls')),
<<<<<<< HEAD
    path('', include('article.urls')),
>>>>>>> parent of 430dda8... Downloading
=======
    path('questionary/', include('questionary.urls')),
    path('', include('article.urls')),
>>>>>>> parent of 34c64c1... asd

]
