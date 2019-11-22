from django.contrib import admin

from .models import One_liner, User

class UserAdmin(admin.ModelAdmin):
    fields = ['user_name']

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'author', 'one_liner_text']
    list_display = ('pub_date', 'author', 'one_liner_text')
    list_filter = ['pub_date']


admin.site.register(One_liner, QuestionAdmin)
admin.site.register(User, UserAdmin)
