from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=80)
    brand=models.CharField(max_length=80,blank=True,null=True,default="")
    image=models.ImageField(upload_to="upload/car") 
    model=models.CharField(max_length=80)
    condition=models.CharField(max_length=255,blank=True,null=True,default="")
    color=models.CharField(max_length=70,blank=True,null=True,default="")
    price=models.IntegerField(default=0)
    plate=models.CharField(blank=True,null=True,max_length=10,default="")
    telegram=models.CharField(max_length=255,blank=True,null=True,default="")
    def __str__(self) -> str:
        return self.brand + " " + self.name + " " + self.model
class YeneUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    photo=models.ImageField(upload_to='upload/profile')
    def __str__(self) -> str:
        return self.user.username + " " + self.phone

class CarImages(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="cars")
    image=models.ImageField(upload_to="upload/car")
    def __str__(self) -> str:
        return str(self.car) 


class Post(models.Model):
    yeneuser=models.ForeignKey(YeneUser,on_delete=models.CASCADE)
    car=models.OneToOneField(Car,on_delete=models.CASCADE)
    postedAt=models.DateTimeField(default=datetime.datetime.today())
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.yeneuser.user.username + " " + self.car.brand + " " + str(self.postedAt)

    


    