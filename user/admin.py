from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


@admin.register(User)
class UserAdmin (BaseUserAdmin):
    fieldsets=(
        (None,{
        'fields':('username','password')
        }),
        
        ('información personal',{
        'fields':('first_name','last_name','email',)
        }),
        ('Permisos',{
        'fields':(
        'is_superuser',
        'is_staff',
        'is_active'
            ),
        }),
    )