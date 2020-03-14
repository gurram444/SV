from django.db import models
import datetime
# Create your models here.


class Country(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class State(models.Model):
    name=models.CharField(max_length=30)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=40)
    gmail=models.CharField(max_length=60)
    street=models.CharField(max_length=200)
    street2=models.CharField(max_length=200)
    zip=models.IntegerField()
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    id_proof=models.CharField(max_length=200)
    proof_no=models.IntegerField()

    def __str__(self):
        return self.name


class Visit(models.Model):
    name=models.ForeignKey(Visitor,on_delete=models.CASCADE)
    place=models.CharField(max_length=100)
    check_in = models.DateTimeField(auto_now=True)
    check_out = models.DateTimeField(auto_now=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=60)
    gender=models.CharField(max_length=30)
    phone = models.CharField(max_length=40)
    gmail = models.CharField(max_length=60)
    qualification=models.CharField(max_length=200)
    designation=models.CharField(max_length=40)

    def __str__(self):
        return self.name




