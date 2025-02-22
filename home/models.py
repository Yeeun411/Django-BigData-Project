from django.db import models

# Create your models here.

class HouseTable(models.Model):
    #idx = models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)
    idx = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    jibun = models.CharField(max_length=100, null=True)
    jungong = models.CharField(max_length=50)
    houseType = models.CharField(max_length=10)
    floors = models.SmallIntegerField()
    housePrice = models.IntegerField(null=True)
    monthlyPrice = models.IntegerField(null=True)
    memePrice = models.IntegerField(null=True)
    currentlyUpdate = models.CharField(max_length=50)
    firstUpdate = models.CharField(max_length=50)
    recommend = models.BooleanField()
    agentName = models.CharField(max_length=100)
    agentAddress = models.CharField(max_length=100)
    agentNumber = models.CharField(max_length=100)
    latitude = models.CharField(max_length=30, default='')
    longtitude = models.CharField(max_length=30, default='')