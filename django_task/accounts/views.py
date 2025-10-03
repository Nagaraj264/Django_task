from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from .forms import SignupForm, LoginForm

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)  # Log user in after signup
            if user.role == "patient":
                return redirect("patient-dashboard")
            return redirect("doctor-dashboard")
        return render(request, "accounts/signup.html", {"form": form})

@login_required
def patient_dashboard(request):
    user = request.user
    return render(request, "accounts/dashboard_patient.html", {"user_obj": user})

@login_required
def doctor_dashboard(request):
    user = request.user
    return render(request, "accounts/dashboard_doctor.html", {"user_obj": user})

def logout_view(request):
    logout(request)
    return redirect("signup")

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.role == "patient":
                return redirect("patient-dashboard")
            return redirect("doctor-dashboard")
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == "patient":
                    return redirect("patient-dashboard")
                return redirect("doctor-dashboard")
        return render(request, "accounts/login.html", {"form": form})
