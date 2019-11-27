from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, One_liner

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'telegram_uuid4']

admin.site.register(CustomUser, CustomUserAdmin)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'author', 'one_liner_text']
    list_display = ('pub_date', 'author', 'one_liner_text')
    list_filter = ['pub_date']


admin.site.register(One_liner, QuestionAdmin)
# admin.site.register(User, UserAdmin)
