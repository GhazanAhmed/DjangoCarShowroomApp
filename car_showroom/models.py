from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class ShowRoom(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
      verbose_name_plural='Showroom'

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    pics = models.ImageField(null=True, blank=True)
    role = models.CharField(max_length=100)
    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)

    class Meta:
      verbose_name_plural='Staff'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    engine = models.OneToOneField('Engine', primary_key=True, on_delete=models.CASCADE)
    features = models.ManyToManyField('Feature')

    def __str__(self):
        return self.name

class Engine(models.Model):
    engine_number = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=80, null=True)
    specs = models.CharField(max_length=150, null=True)


    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    chassis_number = models.CharField(max_length=100, primary_key=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.chassis_number
