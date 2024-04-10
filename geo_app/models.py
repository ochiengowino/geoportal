# from django.db import models
from django.contrib.gis.db import models
from django.db.models.signals import post_save, post_delete
import os
from geo.Geoserver import Geoserver
from django.dispatch import receiver

geo = Geoserver('http://127.0.0.1:8090/geoserver/', username='admin', password='geoserver')
workspace = 'geoportal'

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email= models.EmailField()
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()

class UserPassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=100)

class Counties(models.Model):
    county = models.CharField(max_length=20, null=True)
    total_pop = models.BigIntegerField(null=True)
    covidcases = models.IntegerField(null=True)
    geom = models.MultiPolygonField(srid=-1)

    def __str__(self): return self.county


class Raster(models.Model):
    raster_name = models.CharField(max_length=50, null=True)
    resolution = models.FloatField(null=True)
    year = models.IntegerField(null=True)
    file = models.FileField(upload_to='Rasters/', null=True, verbose_name="Tiff")
    sld_file = models.FileField(upload_to='Rasters/Style', null=True, blank=True, verbose_name="sld")
    uploaded_date = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = "Rasters"
        def __str__(self):
            return self.raster_name

@receiver(post_save, sender=Raster)

def publish_raster(sender, instance, created, **kwargs):
    file=instance.file.path
    file_info = os.path.basename(file).split('.')
    file_format = file_info[-1]
    file_name = file_info[0]
    file_path = os.path.dirname(file)

    raster_name_ = instance.raster_name
    year = instance.year
    published_raster_name = f'{raster_name_}_{str(year)}'

    # publish layer
    print('start publish')
    geo.create_coveragestore(file, workspace=workspace, layer_name=published_raster_name)
    sld_file = instance.sld_file.path
    sld_name = os.path.basename(file).split('.')[0]
    geo.upload_style(path=sld_file, workspace=workspace)
    geo.publish_style(layer_name=published_raster_name, style_name=sld_name, workspace=workspace)

    print('done', published_raster_name, sld_name)