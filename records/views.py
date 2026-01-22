from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MedicalRecord
from .forms import MedicalRecordForm

@login_required
def record_list(request):
    if request.user.role == "doctor":
        records = MedicalRecord.objects.filter(doctor=request.user)
    else:
        records = MedicalRecord.objects.filter(patient=request.user.profile)

    return render(request, "record_list.html", {"records": records})


@login_required
def record_create(request):
    if request.user.role != "doctor":
        return redirect("dashboard")

    form = MedicalRecordForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.doctor = request.user
        record.save()
        return redirect("record_list")

    return render(request, "record_create.html", {"form": form})


@login_required
def record_detail(request, id):
    record = MedicalRecord.objects.get(id=id)

    if request.user.role == "patient" and record.patient != request.user.profile:
        return redirect("dashboard")

    return render(request, "record_detail.html", {"record": record})
