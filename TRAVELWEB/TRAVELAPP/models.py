from django.db import models
# Create your models here.

class MyUsers(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.username + '--' + self.email


class SearchHotel(models.Model):
    city=models.CharField(max_length=250)
    checkin=models.DateField()
    checkout=models.DateField()
    no_rooms=models.IntegerField()
    uname=models.CharField(max_length=50)
    def __str__(self):
        return self.city + '--' +str(self.uname)

class BookHotel(models.Model):
    City=models.CharField(max_length=250)
    Address=models.CharField(max_length=250)
    Hotel_name=models.CharField(max_length=250)
    room_type=models.CharField(max_length=250)
    price=models.DecimalField(decimal_places=0,max_digits=10)
    pic=models.ImageField(null=True,blank=True)
    user=models.CharField(max_length=50)


    def __str__(self):
         return self.City + '--' + self.Hotel_name

class ConfirmHotel(models.Model):
    name=models.CharField(max_length=250)
    indate=models.CharField(max_length=250)
    outdate=models.CharField(max_length=250)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()
    room_type=models.CharField(max_length=250)
    payment=models.CharField(max_length=10)
    total=models.DecimalField(max_digits=10,decimal_places=3)

class PBook(models.Model):
    Pname=models.CharField(max_length=250)
    duration=models.CharField(max_length=250)
    inclusions=models.CharField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=3)
    user=models.CharField(max_length=50)
    pic=models.ImageField(null=True,blank=True)

class PConfirm(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    no_of_days= models.CharField(max_length=250)
    payment = models.CharField(max_length=10)
    total = models.CharField(max_length=250)

class SearchFlight(models.Model):
    boarding=models.CharField(max_length=250)
    destination=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    seats=models.IntegerField()
    date=models.DateField()
    user=models.CharField(max_length=50)

class FlightInfo(models.Model):
    airline=models.CharField(max_length=250)
    departure=models.CharField(max_length=250)
    arrival=models.CharField(max_length=250)
    price=models.IntegerField()
    username=models.CharField(max_length=250)

class Fconfirm(models.Model):
    payment=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    bill=models.DecimalField(max_digits=10,decimal_places=3)
    username=models.CharField(max_length=50)


class Review(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mail = models.CharField(max_length=250)
    review = models.CharField(max_length=300)
    stars = models.CharField(max_length=10)

    def __str__(self):
        return self.fname + '--' + self.review