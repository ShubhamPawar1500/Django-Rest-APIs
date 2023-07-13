from django.db import models

# Create your models here.

class FileData(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
