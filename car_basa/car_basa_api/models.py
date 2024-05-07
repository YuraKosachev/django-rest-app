from django.db import models

# Create your models here.


class Brand(models.Model):
    brand = models.CharField(max_length=60)

class Mark(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    mark = models.CharField(max_length=60)

class Generation(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
    generation = models.CharField(max_length=60)
    year_start = models.IntegerField()
    year_end = models.IntegerField()

class Carcase(models.Model):
    carcase = models.CharField(max_length=60)

class Engine(models.Model):
    engine = models.CharField(max_length=60)

class Drive(models.Model):
    drive = models.CharField(max_length=60)

class Transmission(models.Model):
    transmission = models.CharField(max_length=60)

class Advertisement(models.Model):
    generation = models.ForeignKey(Generation, on_delete=models.PROTECT)
    volume = models.DecimalField(max_digits=3, decimal_places=1)
    year = models.IntegerField()
    price_usd = models.DecimalField(max_digits=12, decimal_places=2)
    carcase = models.ForeignKey(Carcase, on_delete=models.PROTECT)
    engine = models.ForeignKey(Engine, on_delete=models.PROTECT)
    drive = models.ForeignKey(Drive, on_delete=models.PROTECT)
    transmission = models.ForeignKey(Transmission,on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    region = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    av_id = models.IntegerField()


class Image(models.Model):
    av_id = models.IntegerField()
    mime_type = models.CharField()
    is_main = models.BooleanField(default=False)
    height_small = models.IntegerField()
    width_small = models.IntegerField()
    url_small = models.CharField()
    height_big = models.IntegerField()
    width_big = models.IntegerField()
    url_big = models.CharField()
    height_extrasmall = models.IntegerField()
    width_extrasmall= models.IntegerField()
    url_extrasmall = models.CharField()
    height_medium = models.IntegerField()
    width_medium = models.IntegerField()
    url_medium = models.CharField()
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
