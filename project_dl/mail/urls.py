from django.urls import path, include, re_path
import mail.views
urlpatterns = [
    path('addwork/', mail.views.upload_file),
    path('', mail.views.uploaded_file),
]