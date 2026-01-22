from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Role_Choices = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('receptionist', 'Receptionist'),
        ('patient', 'Patient'),
    )

    role = models.CharField(max_length=20, choices=Role_Choices)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_image = models.ImageField(upload_to='patients/', blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    hospital_name = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    blood_group = models.CharField(max_length=5, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

