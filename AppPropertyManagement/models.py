from django.db import models

# Create your models here.
class admindata(models.Model):
    Username = models.CharField(max_length=100 ,default = None)
    Password = models.CharField(max_length=100 ,default = None)

    class Meta:
        db_table = 'admindata'

class UserRegisters(models.Model):
    Name = models.CharField(max_length=100 ,default = None)
    Address = models.CharField(max_length=100 ,default = None)
    Mobile =  models.CharField(max_length=100 ,default = None)
    Email = models.CharField(max_length=100 ,default = None)
    Username = models.CharField(max_length=100 ,default = None)
    Password = models.CharField(max_length=100 ,default = None)

    class Meta:
        db_table = 'UserRegisters'

class PropertyDetails(models.Model):
    Type = models.CharField(max_length=100 ,default = None)
    Sqft = models.IntegerField(default = None)
    PropertyType= models.CharField(max_length=100 ,default = None)
    Area=models.CharField(max_length=100,default = None )
    Address = models.CharField(max_length=100 ,default = None)
    Landmark = models.CharField(max_length=100 ,default = None)
    DeveloperName = models.CharField(max_length=100 ,default = None)
    Price = models.CharField(max_length=100 ,default = None)
    Bedroom = models.IntegerField(default = None)
    Bathroom = models.IntegerField(default = None)
    Furnished = models.CharField(max_length = 100 ,default = None)
    Parking = models.CharField(max_length = 100 ,default = None)
    CCTV = models.CharField(max_length=100 ,default = None)
    Image = models.ImageField(upload_to='static/Images', default = None)
    
    class Meta:
        db_table = 'PropertyDetails'

class Favaourite(models.Model):
    PropertyID=models.IntegerField(default = None)
    UserID=models.IntegerField(default = None)
    P_Type = models.CharField(max_length=100 ,default = None)
    Sqft = models.IntegerField(default = None)
    Area=models.CharField(max_length=100,default = None )
    Price = models.CharField(max_length=100 ,default = None)

    class Meta:
        db_table = 'Favaourite'

class Appointment(models.Model):
    User_ID=models.IntegerField(default = None)
    Property_ID=models.IntegerField(default=None)
    Area=models.CharField(max_length=100,default = None )
    Price = models.CharField(max_length=100 ,default = None)
    Date=models.CharField(max_length=100 ,default = None)

    class Meta:
        db_table = 'Appointment'

class Advertisements(models.Model):
    Name=models.CharField(max_length=100,default=None)
    AdsImage = models.ImageField(upload_to='static/Images', default = None)

    class Meta:
        db_table = 'Advertisements'

class DigitalProperty(models.Model):
    Type = models.CharField(max_length=100 ,default = None)
    Link= models.CharField(max_length=500 ,default = None)
    Image = models.ImageField(upload_to='static/Images', default = None)
    
    class Meta:
        db_table = 'Digital Property'