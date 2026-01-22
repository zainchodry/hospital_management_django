from django.db import models
from accounts.models import User, Profile

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'doctor'})

    diagnosis = models.TextField()
    prescription = models.TextField()
    notes = models.TextField(blank=True)

    report_file = models.FileField(upload_to="reports/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.created_at.date()}"
