from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(default = 'default.jpg', upload_to = 'student_pics')