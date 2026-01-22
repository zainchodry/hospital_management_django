from django.db import models
from accounts.models import User, Profile

class Appointment(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    patient = models.ForeignKey(Profile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'doctor'})

    date = models.DateField()
    time = models.TimeField()

    reason = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.date}"
