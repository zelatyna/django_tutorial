from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, One_liner

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'phone_number']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'phone_number'),
        }),
    )


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'author', 'one_liner_text']
    list_display = ('pub_date', 'author', 'one_liner_text')
    list_filter = ['pub_date']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(One_liner, QuestionAdmin)

# admin.site.register(User, UserAdmin)
