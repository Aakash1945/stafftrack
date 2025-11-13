from django.shortcuts import render,HttpResponse



# Create your views here.
def index(request):
    return render(request,"index.html")

def attendance_page(request):
    return render(request, "tracking.html")

def payment_page(request):
    return render(request, "payment.html")

def role_page(request):
    return render(request, "role.html")

def report_page(request):
    return render(request, "report.html")


