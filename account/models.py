from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50, default='default')
    id = models.IntegerField(primary_key=True, unique=True)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100, default='default_password')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True, unique=True)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100, default='default_password')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


    def __str__(self):
        return self.name
    

class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student.name}'s {self.course_name}"

    @classmethod
    def create_registration(cls, student, course_name):
        """
        Method to create a new CourseRegistration entry.
        """
        return cls.objects.create(student=student, course_name=course_name)
