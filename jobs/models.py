from django.db import models
class Job(models.Model):
    Image = models.ImageField(upload_to='images/')
    Summary = models.CharField(max_length=200)
# Create your models here.
