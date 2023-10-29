from django.db import models
from django.utils import timezone

# Create your models here.
class Year(models.Model):
    Year = models.IntegerField()

    def __str__(self):
        return str(self.Year)

class Date_Application(models.Model):
    Year = models.ForeignKey(Year,on_delete=models.CASCADE)
    # Date=models.DateTimeField(null=True,default=timezone.now)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    Reqruipment_Title = models.CharField(max_length=200)

    def __str__(self):
        return self.Reqruipment_Title
    
class Applicant(models.Model):
    First_Name = models.CharField(max_length=100)
    Second_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    job_role = models.CharField(null=True,blank=True,max_length=200)
    Linkedin_Profile = models.CharField(max_length=500)
    Github_Profile = models.CharField(max_length=500)
    Twitter_Profile = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.Email