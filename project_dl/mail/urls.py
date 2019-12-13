from django.urls import path, include, re_path
import mail.views
urlpatterns = [
<<<<<<< HEAD
    path('', mail.views.upload_file),
    path('addwork/', mail.views.upload_file),
=======
    path('addwork/', mail.views.upload_file),
    path('', mail.views.uploaded_file),
>>>>>>> parent of 34c64c1... asd
]