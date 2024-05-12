import re

from django.db import models

d_choices = [
    ('IT', 'Information Technology'),
    ('HR', 'Human Resources'),
    ('fin', 'Finance'),
    ('sales', 'Sales'),
    ('accounts', 'Accounts'),

]

r_choices = [
    ('manager', 'Manager'),
    ('developer', 'Developer'),
    ('analyst', 'Analyst'),
    ('assistant', 'Assistant'),
]

def check_number(value):
    pattern=r'^\+?91?[0-9]{10}$'
    if re.match(pattern, value):
        return True, "Valid phone number."
    else:
        return False, "Invalid phone number. Please provide a valid Indian phone number starting with '+91'."


class Assistant(models.Model):
    id = models.AutoField( primary_key=True)
    name= models.CharField(max_length=100)
    mobile = models.CharField(max_length=13,validators=[check_number])
    email = models.EmailField(max_length=100)
    salary = models.DecimalField(max_digits=20,decimal_places=2)
    department = models.CharField(max_length=50,choices=d_choices)
    role = models.CharField(max_length=50,choices=r_choices)
    city = models.CharField(max_length=100,null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)

