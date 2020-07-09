#django
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def upload_picture_user():
    pass

def upload_picture_order():
    pass

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    birthdate = models.DateField( auto_now=False, auto_now_add=False)
    picture = models.FileField( upload_to=None, max_length=100)

    USERNAME_FIELD = 'email' #to login - as uniquefield
    REQUIRED_FIELDS = ['name', 'birthdate'] #when createsuperuser


class Document(models.Model):
    DT = (
        ('rg', 'rg'),
        ('cpf', 'cpf')
    )
    document_type = models.CharField(choices=DT, max_length=3)
    document_number = models.CharField(max_length=20)

class Customer(User):
    document = models.ForeignKey('Document', on_delete=models.CASCADE)


