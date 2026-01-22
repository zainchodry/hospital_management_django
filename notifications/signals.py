from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from records.models import MedicalRecord
from .models import Notification
from django.core.mail import send_mail

@receiver(post_save, sender=Appointment)
def appointment_notify(sender, instance, created, **kwargs):
    if instance.status == "approved":
        user = instance.patient.user

        msg = f"Your appointment with Dr. {instance.doctor.username} on {instance.date} is approved."

        Notification.objects.create(user=user, message=msg)

        send_mail(
            "Appointment Approved",
            msg,
            "hospital@system.com",
            [user.email],
            fail_silently=True,
        )


@receiver(post_save, sender=MedicalRecord)
def record_notify(sender, instance, created, **kwargs):
    if created:
        user = instance.patient.user
        msg = "A new medical record has been added to your profile."

        Notification.objects.create(user=user, message=msg)

        send_mail(
            "New Medical Record",
            msg,
            "hospital@system.com",
            [user.email],
            fail_silently=True,
        )
