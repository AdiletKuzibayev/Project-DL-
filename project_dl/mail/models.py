from django.db import models

# Create your models here.
class Homework(models.Model):
    class Meta:
        db_table = "homework"
    work_title = models.CharField(max_length=200)
    work_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

