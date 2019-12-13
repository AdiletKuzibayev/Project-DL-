from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from .validators import validate_file_extension
# Create your models here.
from datetime import datetime
>>>>>>> parent of 34c64c1... asd
class Homework(models.Model):
    class Meta:
        db_table = "homework"
    work_title = models.CharField(max_length=200)
<<<<<<< HEAD
    work_file = models.FileField(upload_to='uploads/%Y/%m/%d/')
=======
    work_file = models.FileField(upload_to='media/%Y/%m/%d/', validators=[validate_file_extension])
    work_date = models.DateTimeField(default=datetime.now())
>>>>>>> parent of 34c64c1... asd

