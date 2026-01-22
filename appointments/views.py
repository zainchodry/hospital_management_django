from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm

@login_required
def appointment_list(request):
    if request.user.role == "patient":
        appointments = Appointment.objects.filter(patient=request.user.profile)
    else:
        appointments = Appointment.objects.filter(doctor=request.user)

    return render(request, "appointment_list.html", {"appointments": appointments})


@login_required
def appointment_create(request):
    if request.user.role != "patient":
        return redirect("dashboard")

    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        appt = form.save(commit=False)
        appt.patient = request.user.profile
        appt.save()
        return redirect("appointment_list")

    return render(request, "appointment_create.html", {"form": form})


@login_required
def appointment_manage(request, id):
    if request.user.role != "doctor":
        return redirect("dashboard")

    appt = Appointment.objects.get(id=id)

    if request.method == "POST":
        appt.status = request.POST['status']
        appt.save()
        return redirect("appointment_list")

    return render(request, "appointment_manage.html", {"appt": appt})
