# from rest_framework import serializers
from .models import Counties
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class countiesSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Counties
        geo_field = "geom"
        fields = "__all__"