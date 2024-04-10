from geo.Geoserver import Geoserver

geo = Geoserver('http://127.0.0.1:8090/geoserver/', username='admin', password='geoserver')

# geo.create_workspace(workspace='geoportal')

# geo.create_coveragestore(layer_name='kenya_srtm_layer', path=r'C:\xampp\htdocs\geoportal\geoportal\data\Kenya_SRTM30m\Kenya_SRTM30meters.tif', workspace='geoportal')

# For creating postGIS connection and publish postGIS table
# geo.create_featurestore(store_name='geo_data1', workspace='geoportal', db='geoportal_db', host='127.0.0.1', pg_user='postgres',
#                         pg_password='geospatial')
# geo.publish_featurestore(workspace='geoportal', store_name='geo_data1', pg_table='kenya_counties')

# For uploading SLD file and connect it with layer
# geo.upload_style(path=r'C:\xampp\htdocs\geoportal\geoportal\data\Kenya_SRTM30m\srtm.sld', workspace='geoportal')
# geo.publish_style(layer_name='kenya_srtm_layer', style_name='srtm_style', workspace='geoportal')

# For creating the style file for raster data dynamically and connect it with layer
# geo.create_coveragestyle(raster_path=r'C:\xampp\htdocs\geoportal\geoportal\data\Kenya_SRTM30m\Kenya_SRTM30meters.tif', style_name='srtm_style', workspace='geoportal',
#                          color_ramp='RdYiGn')
# geo.publish_style(layer_name='kenya_srtm_layer', style_name='srtm_style', workspace='geoportal')

# delete workspace
# geo.delete_workspace(workspace='geoportal')

# # delete layer
# geo.delete_layer(layer_name='agri_final_proj', workspace='geoportal')

# # delete style file
# geo.delete_style(style_name='kamal2', workspace='geoportal')