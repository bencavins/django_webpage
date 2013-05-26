from django.contrib import admin
from resume.models import Resume

# Class definitions for admin models
class ResumeAdmin(admin.ModelAdmin):
    
    contact_info_fieldsets_dict = {
        'fields': [
            'first_name',
            'last_name',
            'address_line1',
            'address_line2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
        ],
    }

    date_info_fieldsets_dict = {
        'fields': [
            'create_datetime',
            'last_modified_datetime',
        ],
    }
    
    fieldsets = [
        ('Contact Info', contact_info_fieldsets_dict),
        ('Date Information', date_info_fieldsets_dict),
    ]

# Register admin models
admin.site.register(Resume, ResumeAdmin)
