import geopandas as gpd 
import json
from django.core.serializers import serialize
from geo.Geoserver import Geoserver
from .models import Raster
from pathlib import Path
from . import sld_products

import random 
import string

# import environ
import os

# env = environ.Env()

# environ.Env.read_env(env_file=".env")


def get_wkt(feature):
    """Generates wkt from a feature collection"""
    geodataframe = gpd.GeoDataFrame.from_features(feature)

    wkt_file = geodataframe.geometry.to_wkt()

    wkt_string = ""

    for data in wkt_file:
        wkt_string += data
    
    return wkt_string


def get_geojson_from_db(code):
    county = Raster.objects.filter(code=code)
    county = serialize('geojson', county)
    county = json.loads(county)

    return county

def get_geojson(jsonstring):
    """this funtion returns geojson feature collection from a string"""
    geojson = json.loads(jsonstring)

    formated_geojson = dict(type="FeatureCollection",features=
                            [dict(geometry=geojson,properties=dict())])
    
    return formated_geojson


def get_random_name(name):
    letters = string.ascii_lowercase
    random_letters = ''.join(random.choice(letters) for i in range(10))

    return name+"_"+ random_letters

sld_path = Path(__file__).resolve().parent /  'Data/styles'

sld_path = str(sld_path)

def get_sldfile(indicator,sub_indicator=None,geometry=None,custom=False,area_code=None):
    if custom == False:
        geometry = get_geojson_from_db(area_code)
    
    if custom == True:
        geometry = get_geojson(geometry)
        area_code = get_random_name(area_code)


    
    sld_rule = sld_products.sld_products.get(indicator,None)
    sld_rule = sld_rule.get(sub_indicator,None)
    sld_rule = sld_rule.get('sld_rule', None)
    sld_start = sld_products.sld_start
    sld_middle = sld_products.sld_middle
    sld_end = sld_products.sld_end

    wkt_geometry = get_wkt(geometry)

   
    sld_File = sld_path+'/'+indicator+'_'+sub_indicator+'_'+area_code+'.sld'

    sld_name = os.path.basename(sld_File).split('.')[0]
    
    with open(sld_File, 'w') as f:
        f.write(sld_start+wkt_geometry+sld_middle+'\n'+sld_rule+sld_end)
    
    geo = Geoserver('http://127.0.0.1:8090/geoserver',
                username='admin', password='geoserver')
    
   
    geo.upload_style(path=sld_File, workspace='geoportal')
    # geo.publish_style(layer_name=area_code+product, style_name=sld_name, workspace='wemast_datasets') 

    

    return sld_name
    
