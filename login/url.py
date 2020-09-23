from django.urls import path
from django.contrib.auth import views
from . import views as views_app
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.LoginView.as_view(
        template_name='login/login.html'), name='login'),
    path('home/', views_app.home, name='home'),
    path('addemployee/', TemplateView.as_view(template_name='login/addemployee.html'),
         name='addemployee'),
    path('employee_added/', views_app.employee_added, name='employee_added'),
    path('showemployee', views_app.showEmployee, name='showEmployee'),
    path('sendemail', views_app.sendEmail, name='sendEmail'),
]
