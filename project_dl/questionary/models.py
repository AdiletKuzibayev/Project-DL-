from django.db import models

# Create your models here.
class Questions(models.Model):
    class Meta:
        db_table = "questionary"
    completed = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)

