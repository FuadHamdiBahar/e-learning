from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    credit = models.IntegerField()
    
    
    def __str__(self):
        return self.title