from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Administration(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


    def __str__(self):
        return self.name
    
class AppliedLeave(models.Model):
    student_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

