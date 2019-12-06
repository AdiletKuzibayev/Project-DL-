from django.db import models
from .validators import validate_file_extension
# Create your models here.
from datetime import datetime
class Homework(models.Model):
    class Meta:
        db_table = "homework"
    work_title = models.CharField(max_length=200)
    work_file = models.FileField(upload_to='media/%Y/%m/%d/', validators=[validate_file_extension])
    work_date = models.DateTimeField(default=datetime.now())

