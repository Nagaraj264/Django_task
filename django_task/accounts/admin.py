from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Profile", {"fields": ("role","profile_picture","address_line1","city","state","pincode")}),
    )
    list_display = ("username","email","first_name","last_name","role","is_staff")
    search_fields = ("username","email","first_name","last_name")
