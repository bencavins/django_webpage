from django.contrib import admin
from resume.models import Resume, Employer, Position

# Class definitions for admin models

class EmployerInline(admin.StackedInline):
    
    model = Employer
    extra = 1
    employer_fields = [
        'name',
        'address_line1',
        'address_line2',
        'city',
        'state',
        'zip_code',
    ]
    fieldsets = [(None, {'fields': employer_fields})]

class ResumeAdmin(admin.ModelAdmin):
    
    contact_info_fields = [
        'first_name',
        'last_name',
        'address_line1',
        'address_line2',
        'city',
        'state',
        'zip_code',
        'phone_number',
        'email',
    ]

    date_info_fields = [
        'create_datetime',
        'last_modified_datetime',
    ]
    
    fieldsets = [
        ('Contact Info', {'fields': contact_info_fields}),
        ('Date Information', {'fields': date_info_fields}),
    ]
    
    inlines = [EmployerInline]


# Register admin models
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Employer)
admin.site.register(Position)
