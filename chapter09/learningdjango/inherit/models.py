from django.db import models

# Create your models here.

# ABS
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

class Employee(CommonInfo):
    company = models.CharField(max_length=16)


# Multi table

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()

class Office(Place):
    has_meeting_rooms = models.BooleanField()


# Proxy
