from django.db import models


class Resume(models.Model):
    
    # Constants
    MAX_NAME_LEN  = 32
    MAX_ADDR_LEN  = 124
    MAX_CITY_LEN  = 32
    MAX_STATE_LEN = 16
    MAX_ZIP_LEN   = 16
    MAX_PHONE_LEN = 16
    MAX_EMAIL_LEN = 256

    # Fields
    first_name    = models.CharField(max_length=MAX_NAME_LEN)
    last_name     = models.CharField(max_length=MAX_NAME_LEN)
    address_line1 = models.CharField(max_length=MAX_ADDR_LEN)
    address_line2 = models.CharField(max_length=MAX_ADDR_LEN)
    city          = models.CharField(max_length=MAX_CITY_LEN)
    state         = models.CharField(max_length=MAX_STATE_LEN)
    zip_code      = models.CharField(max_length=MAX_ZIP_LEN)
    phone_number  = models.CharField(max_length=MAX_PHONE_LEN)
    email         = models.EmailField(max_length=MAX_EMAIL_LEN)
    create_datetime        = models.DateTimeField()
    last_modified_datetime = models.DateTimeField()

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Employer(models.Model):

    MAX_NAME_LEN  = 124
    MAX_ADDR_LEN  = 124
    MAX_CITY_LEN  = 32
    MAX_STATE_LEN = 16
    MAX_ZIP_LEN   = 16
    
    resume        = models.ForeignKey(Resume)
    name          = models.CharField(max_length=MAX_NAME_LEN)
    address_line1 = models.CharField(max_length=MAX_ADDR_LEN)
    address_line2 = models.CharField(max_length=MAX_ADDR_LEN)
    city          = models.CharField(max_length=MAX_CITY_LEN)
    state         = models.CharField(max_length=MAX_STATE_LEN)
    zip_code      = models.CharField(max_length=MAX_ZIP_LEN)
    
    def __unicode__(self):
        return self.name

class Position(models.Model):

    MAX_TITLE_LEN = 124

    employer = models.ForeignKey(Employer)
    title = models.CharField(max_length=MAX_TITLE_LEN)
    start_date = models.DateField()
    end_date = models.DateField()
