from django.db import models
from account.models import Student, CourseRegistration


# Create your models here.
class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        (0, 'Absent'),
        (1, 'Present'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
    course_name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.date} - {self.student.name} ({self.status})"
