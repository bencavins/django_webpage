from django.contrib import admin
from resume.models import Resume, Employer, Position, Education

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

class EducationInline(admin.StackedInline):

    model = Education
    extra = 1
    education_fields = [
        'name',
        'degree',
        'city',
        'state',
        'graduation_date',
    ]
    fieldsets = [(None, {'fields': education_fields})]

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
    
    inlines = [EmployerInline, EducationInline]

    list_display = ('get_full_name','create_datetime')


# Register admin models
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Employer)
admin.site.register(Position)
admin.site.register(Education)
