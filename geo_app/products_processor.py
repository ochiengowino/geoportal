
from . import raster_products

from . models import RasterDatasets

def get_list(data, colum):
    list_data = list(data.values_list(colum, flat=True))

    list_data = list(dict.fromkeys(list_data))
    if list_data == [""]:
        return []

    return list_data

def getdata_available(data):

    data_structure = dict(indicators={})

    available_structure = raster_products.products

    for indicator in available_structure['indicators']:
        data_structure['indicators'] = {indicator:{}}

        # print(indicator, 'indicator', data_structure)

        
        indicator_data = data.filter(indicator__contains=indicator)

        for sub_indicator in available_structure['indicators'][indicator]:

            # print(sub_indicator, 'sub')
            data_structure['indicators'][indicator][sub_indicator] = {}

            season = available_structure['indicators'][indicator][sub_indicator].get('season', None)
            parameter =  available_structure['indicators'][indicator][sub_indicator].get('parameter', None)

            print(parameter, 'para', available_structure['indicators'][indicator][sub_indicator])

            sub_indicator_data = indicator_data.filter(sub_indicator__contains=sub_indicator)
            
            if season == []:
                sub_indicator_season_data = get_list(sub_indicator_data,'season')
                data_structure['indicators'][indicator][sub_indicator] = {}
                data_structure['indicators'][indicator][sub_indicator]['season'] = sub_indicator_season_data
                available_structure['indicators'][indicator][sub_indicator]['season'] = sub_indicator_season_data
                years = get_list(sub_indicator_data,'year')
                data_structure['indicators'][indicator][sub_indicator]['year'] = years
                available_structure['indicators'][indicator][sub_indicator]['year'] = years
            if parameter == []: 
                sub_indicator_parameter_data = get_list(sub_indicator_data,'parameter')
                data_structure['indicators'][indicator][sub_indicator] = {}
                data_structure['indicators'][indicator][sub_indicator]['parameter'] = sub_indicator_parameter_data
                available_structure['indicators'][indicator][sub_indicator]['parameter'] = sub_indicator_parameter_data
                years = get_list(sub_indicator_data,'year')
                data_structure['indicators'][indicator][sub_indicator]['year'] = years
                available_structure['indicators'][indicator][sub_indicator]['year'] = years
              
            else :
                years = get_list(sub_indicator_data,'year')
                data_structure['indicators'][indicator][sub_indicator]['year'] = years
                available_structure['indicators'][indicator][sub_indicator]['year'] = years

            # print('ggg', years, data_structure)
            
    return available_structure



# test_data = RasterDatasets.objects.all()

# test = getdata_available(test_data)

# print(test, 'fff')



