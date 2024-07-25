from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import User, UserPassword, Counties, Raster
from .serializers import countiesSerializer, RasterSerializer
from . import products_processor, raster_products, sld_processor
from django.core.serializers import serialize
from rest_framework import viewsets
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
import json
# import environ

workspace = 'geoportal'

# Create your views here.

class CountiesViewset(viewsets.ModelViewSet):
    """This class handles regions shapefile"""
    serializer_class = countiesSerializer
    queryset = Counties.objects.all()

    @action(detail=False, methods=['get'])
    @csrf_exempt
    def category1(self, request):

        if request.method == 'GET':
                data = request.GET.copy()
        elif request.method == 'POST':
            data = request.GET.copy()
        else:
            return HttpResponseBadRequest('Only POST and GET methods are supported')

        category_data = Counties.objects.all()

        serialized = serialize('geojson',  category_data)
        
        counties = [json.loads(serialized)]

        # print(regions[0]['features'][0]['geometry'])
        """convert geometry to geom in line with existing system """

        counties_dataset = counties[0]

        counties_data_modified = []
        
        for feature in counties_dataset['features']:
            geom = dict(geometry=feature['geometry'])
            del feature['geometry']
            feature['geom'] = geom['geometry']
            feature['geom']['bbox'] = None
            # print(feature['geom'])
            output_data = dict() 
            for prop in feature['properties']:
               
                output_data[prop] = feature['properties'][prop]
            output_data['geom'] = geom['geometry'] 
            counties_data_modified.append(
                output_data
            )


        return JsonResponse(counties, safe=False)


class RasterViewSet(viewsets.ModelViewSet):
    serializer_class = RasterSerializer
    queryset = Raster.objects.all()
    
    @action(detail=False, methods=['post'])
    @csrf_exempt

    def getdatastorestructure(self, request):
        if request.method == 'POST':
                data = request.GET.copy()
        else:
            return HttpResponseBadRequest('Only POST supported')

        data_available = Raster.objects.all()

        # rasters_available = products_processor.getdata_available(data_available)

        return JsonResponse(data_available, safe=False)
    
    # @action(detail=False, methods=['post', 'get'])
    # @csrf_exempt
    # def productinfo(self, request):

    #     if request.method == 'GET':
    #             data = request.GET.copy()
    #     elif request.method == 'POST':
    #         data = request.GET.copy()
    #     else:
    #         return HttpResponseBadRequest('Only POST and GET methods are supported')
        
    #     sub_indicators = data.get('get_sub_indicators', None)
    #     properties_data = data.get('get_properties_sub_indicator', None)

    #     indicators = list(raster_products.products['indicators'].keys())
    #     indicators = dict(indicators=indicators)
        
    #     if sub_indicators:
    #         # list_sub_indicators =  list(raster_products.products['indicators'][sub_indicators].keys())
    #         sub_indicators_data = Raster.objects.filter(indicator=sub_indicators)

    #         list_sub_indicators = products_processor.get_list(sub_indicators_data,'sub_indicator')

    #         list_sub_indicators = dict(indicator=sub_indicators, sub_indicators=list_sub_indicators)

    #         return JsonResponse(list_sub_indicators, safe=False)
        
    #     if properties_data:
    #         sub_indicator_data = Raster.objects.filter(sub_indicator=properties_data)
    #         parameter = products_processor.get_list(sub_indicator_data,'parameter')
    #         season = products_processor.get_list(sub_indicator_data,'season')

    #         data_properties = dict()
    #         if len(parameter) >0:
    #             data_properties['parameter'] = parameter
    #         if len(season) > 0: 
    #             data_properties['season'] = season
            
    #         if len(season) == 0 and len(parameter) == 0 :
    #             data_properties['properties'] = 'No parameter and season for ' + properties_data +' sub indicator'
            
    #         return JsonResponse(data_properties, safe=False)


    #     return JsonResponse(indicators, safe=False)

    # @action(detail=False, methods=['post', 'get'])
    # @csrf_exempt
    # def getproductinfo_years(self, request):
    #     if request.method == 'GET':
    #             data = request.GET.copy()
    #     elif request.method == 'POST':
    #         data = request.GET.copy()
    #     else:
    #         return HttpResponseBadRequest('Only POST and GET methods are supported')
        
    #     indicator = data.get('indicator', None)
    #     sub_indicator = data.get('sub_indicator', None)
    #     parameter = data.get('parameter', None)
    #     season = data.get('parameter', None)

    #     if not indicator or indicator not in list(raster_products.products['indicators'].keys()):
    #         valid_indicator_str = '","'.join(raster_products.products['indicators'].keys())
    #         return HttpResponseBadRequest(f'The indicator parameter is necessary. Valid indicators '
    #         f'include :"{valid_indicator_str}"')

    #     if not sub_indicator or sub_indicator not in products_processor.get_list(Raster.objects.filter(indicator=indicator),'sub_indicator'):
    #         valid__sub_indicator_str = '","'.join(products_processor.get_list(Raster.objects.filter(indicator=indicator),'sub_indicator'))
    #         return HttpResponseBadRequest(f'The sub_indicator parameter is necessary. Valid available sub_indicators for the {indicator} indicator '
    #         f'include :"{valid__sub_indicator_str}"')
        
    #     raster_data_filtered = Raster.objects.filter(indicator=indicator, sub_indicator=sub_indicator)
    #     years_dataset = dict()
    #     if parameter: 
    #         raster_data_filtered = raster_data_filtered.filter(parameter=parameter)
    #         years_dataset['parameter'] = parameter

    #     if season:
    #         raster_data_filtered = raster_data_filtered.filter(season=season)
    #         years_dataset['season'] = season

    #     years = products_processor.get_list(raster_data_filtered,'year')
    #     years_dataset['years'] = years
        
    #     return JsonResponse(years_dataset, safe=False)

        
        



    # @action(detail=False, methods=['post'])
    # @csrf_exempt
    # def finddata(self,request):
    #     if request.method == 'POST':
    #         data = json.loads(request.body)      
    #     else:
    #         return HttpResponseBadRequest('Only POST supported')

        
    #     region = data.get('region', None)
    #     indicator = data.get('indicator', None)
    #     sub_indicator = data.get('sub_indicator', None)
    #     parameter = data.get('parameter', None)
    #     season = data.get('season', None)
    #     geometry = data.get('geometry', None)
    #     year = data.get('year', None)
        
    #     if not indicator or indicator not in list(raster_products.products['indicators'].keys()):
    #         valid_indicator_str = '","'.join(raster_products.products['indicators'].keys())
    #         return HttpResponseBadRequest(f'The indicator parameter is necessary. Valid indicators '
    #         f'include :"{valid_indicator_str}"')

    #     if not sub_indicator or sub_indicator not in products_processor.get_list(Raster.objects.filter(indicator=indicator),'sub_indicator'):
    #         valid__sub_indicator_str = '","'.join(products_processor.get_list(Raster.objects.filter(indicator=indicator),'sub_indicator'))
    #         return HttpResponseBadRequest(f'The sub_indicator parameter is necessary. Valid available sub_indicators for the {indicator} indicator '
    #         f'include :"{valid__sub_indicator_str}"')   

    #     raster_data_filtered = Raster.objects.filter(indicator=indicator, 
    #                                 sub_indicator=sub_indicator,year=year)
    #     # print(list(raster_data_filtered.values('indicator', 'sub_indicator', 'parameter', 'season')))

    #     if not season:
    #         season = ''
    #     if not parameter:
    #         parameter = ''
        
    #     raster_name = indicator+'_'+str(sub_indicator)+'_'+str(season)+'_'+str(parameter)+'_'+str(year)

    #     custom = False

    #     if region == "custom":

    #         custom = True
          
    #     sld_name = sld_processor.get_sldfile(indicator,sub_indicator,geometry=geometry, custom=custom,area_code=region)

        

    #     wms_data_output = dict()
    #     wms_data_output['geoserver'] = 'http://149.248.57.97:8080/geoserver/wms?'
    #     wms_data_output['wmsurl'] =  workspace+':'+raster_name
    #     wms_data_output['layername'] = workspace+':'+raster_name
    #     wms_data_output['legendurl'] = "REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=20&LAYER="+wms_data_output['layername']+"&LEGEND_OPTIONS=border:true;dx:10;fontSize:11;"
    #     wms_data_output['sldname'] = sld_name
    
    #     # if 
    #     # print(raster_name, 'name')



    #     return JsonResponse(wms_data_output, safe=False)



def counties_api(request):
    if request.method == 'GET':
        counties = Counties.objects.all()
        counties_serializer = countiesSerializer(counties, many=True)
        
        return JsonResponse(counties_serializer.data, safe=False, status=200)
    
def dashboard(request):
    return render(request, 'frontend/index.html')

def home(request):
    return render(request, 'geo_app/index.html')


def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        date_of_birth = request.POST['date_of_birth']


        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )
        return redirect('set_password', user_id=user.user_id)

    return render(request, 'geo_app/signup.html')

def set_password(request, user_id):
    user = User.objects.get(user_id=user_id)
  

    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user_password = UserPassword.objects.create(user=user, password=password)

            # Redirect to the login page after setting the password
            return redirect('login')

    return render(request, 'geo_app/set_password.html', {'first_name': user.first_name, 'user_id': user_id})

def user_login(request):
    # return redirect('login')
    return render(request, 'geo_app/georasters/index.html')

def user_logout(request):
    return redirect('login')

# def dashboard(request):
#     pass