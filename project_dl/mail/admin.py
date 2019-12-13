from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from .models import Homework
# Register your models here.

class HomeworkAdmin(admin.ModelAdmin):
    fields = ['work_title', 'work_file', 'work_date']
    list_filter = ['work_date']


admin.site.register(Homework, HomeworkAdmin)
>>>>>>> parent of 34c64c1... asd
