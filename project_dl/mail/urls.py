from django.urls import path, include, re_path
import mail.views
urlpatterns = [
    path('', mail.views.upload_file),
    path('addwork/', mail.views.upload_file),
]