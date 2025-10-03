# Django Task 1

This is a minimal Django app fulfilling the assignment:

- User types: Patient, Doctor
- Signup form fields: first/last name, profile picture, username, email, password, confirm password, address (line1, city, state, pincode)
- Validation ensures password and confirm match
- Dashboards show the submitted details

## Local setup

1) Create a virtualenv and install dependencies:

   pip install -r requirements.txt

2) Make migrations and migrate:

   python django_task1/manage.py makemigrations
   python django_task1/manage.py migrate

3) Run the dev server:

   python django_task1/manage.py runserver

4) Open http://127.0.0.1:8000/ to sign up. You’ll be redirected to the appropriate dashboard.
