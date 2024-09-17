from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    ISDelete=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
