from django.contrib import admin
from .models import PhoneBook,User
from django.contrib.auth.models import Group


class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ( 
                    'first_name', 
                    'last_name', 
                    'phone_number',
                    'email',
                    'city', 
                    'age',
                    'gender',
                    'work_status',
                    'employment_date',
                    'date_of_dismissal',
                    )
    list_display_links = ('phone_number','first_name',)
    search_fields = ('first_name', 'last_name', 'city', 'age')


admin.site.register(PhoneBook, PhoneBookAdmin)

admin.site.register(User)

admin.site.unregister(Group)
