from django.contrib import admin
from resume.models import Resume, Employment

# Class definitions for admin models

class EmploymentInline(admin.StackedInline):
    model = Employment
    extra = 1
    employment_fields = [
        'employer_name',
        'address_line1',
        'address_line2',
        'city',
        'state',
        'zip_code',
        'start_date',
    ]
    fieldsets = [
        (None, {'fields': employment_fields}),
    ]

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
    
    inlines = [EmploymentInline]


# Register admin models
admin.site.register(Resume, ResumeAdmin)

