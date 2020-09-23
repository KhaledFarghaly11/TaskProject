from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'home.html')


def employee_added(request):
    employee = Employee()
    if request.method == "POST":
        myEmployeeForm = EmployeeForm(request.POST)
        if myEmployeeForm.is_valid():
            print("####")
            employee.name = myEmployeeForm.cleaned_data['name']
            employee.iD = myEmployeeForm.cleaned_data['id']
            employee.email = myEmployeeForm.cleaned_data['email']
            employee.picture = myEmployeeForm.cleaned_data['picture']
            employee.salary = myEmployeeForm.cleaned_data['salary']
            employee.save()
            messages.success(request, ("New Employee Added!"))
            return render(request, 'login/addemployee.html')
    else:
        myEmployeeForm = EmployeeForm()
    return render(request, 'login/addemployee.html')


def showEmployee(request):
    emp = Employee.objects.all()
    context = {'employee': emp}
    return render(request, 'login/showemployee.html', context)


def sendEmail(request):
    employee = Employee.objects.all()
    for x in employee:
        send_mail("Header", "Body", "khaledtest70@gmail.com",
                  [x.email], fail_silently=False)
    return render(request, 'login/emailsent.html')
