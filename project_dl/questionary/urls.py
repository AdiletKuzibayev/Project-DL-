from django.urls import path, include

import questionary.views

urlpatterns = [
    path('', questionary.views.questions),
    path('save_questionary/', questionary.views.questions),

]