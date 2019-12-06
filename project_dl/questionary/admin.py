from django.contrib import admin

from .models import Questions
# Register your models here.

class QuestionaryAdmin(admin.ModelAdmin):
    fields = ['completed', 'created_at']
    list_filter = ['created_at']


admin.site.register(Questions, QuestionaryAdmin)