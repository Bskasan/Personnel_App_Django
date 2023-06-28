from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=64)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Personal(models.Model):

    # ------------------- #
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'Prefer Not To Say'),
    )

    TITLES = (
        ('S', 'Senior'),
        ('M', 'Mid-Senior'),
        ('J', 'Junior'),
        ('I', 'Intern'),
    )
    # ------------------- #

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDERS)
    title = models.CharField(max_length=1, choices=TITLES)
    salary = models.IntegerField()
    started_date = models.DateField()
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='personal')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name} - {self.title}"


