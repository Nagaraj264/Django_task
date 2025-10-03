from django.urls import path
from .views import SignupView, LoginView, patient_dashboard, doctor_dashboard, logout_view

urlpatterns = [
    path("", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/patient/", patient_dashboard, name="patient-dashboard"),
    path("dashboard/doctor/", doctor_dashboard, name="doctor-dashboard"),
    path("logout/", logout_view, name="logout"),
]
