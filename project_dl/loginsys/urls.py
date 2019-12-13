from django.urls import path, include

import loginsys.views

urlpatterns = [
    path('login/', loginsys.views.login),
    path('logout/', loginsys.views.logout),
    path('signup/', loginsys.views.signup),
]