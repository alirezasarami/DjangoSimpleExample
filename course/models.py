from django.db import models
# Create your models here.

class Departman(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=10)
    name =models.CharField(max_length=20)
    department = models.ForeignKey(Departman , null=True , on_delete=models.DO_NOTHING , related_name='course_department')
    logo = models.CharField(max_length=255 , default='/media/course_logo/index.png')


















































