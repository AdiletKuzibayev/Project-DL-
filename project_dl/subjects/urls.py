from django.urls import path, include

import subjects.views

urlpatterns = [
    path('', subjects.views.students),
    path('subjects/<int:page_number>/', subjects.views.students),
    path('subjects/get/<int:student_id>/', subjects.views.student),
    path('subjects/addfeedback/<int:student_id>/', subjects.views.addFeedback),
    path('subjects/addmark/<int:student_id>/', subjects.views.addmark),
    path('page/<int:page_number>/', subjects.views.students),

]