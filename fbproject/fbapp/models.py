from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class UserDetails(models.Model):
    first_name    = models.CharField(max_length=30)
    last_name     = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender        = models.CharField(max_length=10)
    fk_login      = models.ForeignKey(Login, on_delete=models.CASCADE)

class UploadImage(models.Model):
    image    = models.FileField(upload_to = 'image/')
    fk_login = models.ForeignKey(Login, on_delete=models.CASCADE)

class AddFriend(models.Model):
    sender_id   = models.IntegerField(max_length=20)
    receiver_id = models.IntegerField(max_length=20)
    status      = models.CharField(max_length=50)
    fk_login    = models.ForeignKey(Login, on_delete=models.CASCADE)