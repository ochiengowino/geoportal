// var map = L.map('map').setView([1.2921, 36.8219], 6);
var osm_layer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});
// osm_layer.addTo(map);


// get capabilities request
// http://localhost:8090/geoserver/wms?service=wms&version=1.1.1&request=GetCapabilities

// get map request
var wms_url = 'http://127.0.0.1:8090/geoserver/geoportal/wms?service=WMS&version=1.1.0&request=GetMap&layers=geoportal%3Akenya_srtm_layer1&bbox=33.90958333333333%2C-4.720694444444433%2C41.887638888888866%2C4.634027777777764&width=654&height=768&srs=EPSG%3A4326&styles=&format=application/json';
// wfs_url = 'http://127.0.0.1:8090/geoserver/geoportal/wms?service=WMS&version=1.1.0&request=GetMap&layers=geoportal%3Akenya_counties&bbox=33.9118156433105%2C-4.70227098464966%2C41.9062576293945%2C5.43064880371094&width=605&height=768&srs=EPSG%3A4326&styles=&outputFormat=application/json';
var wfs_url = 'http://127.0.0.1:8090/geoserver/geoportal/wfs?service=WMS&version=1.1.0&request=GetFeature&layers=geoportal%3Akenya_counties&format=application/json';
var wfs1 =     "http://127.0.0.1:8090/geoserver/wfs?service=wfs&version=1.1.0&request=GetFeature&typeNames=geoportal:kenya_counties&outputFormat=application/json&srsName=epsg:4326";

var srtm_layer = L.tileLayer.wms('http://localhost:8090/geoserver/wms', {
  // layers: 'geoportal:kenya_srtm_layer1',
  layers:"Nzoia:Kenya_SRTM_layer",
  format: 'image/png',
  transparent: true,
  attribution: 'Kenya SRTM Layer'
});

// var county_value;
$.ajax('http://127.0.0.1:8090/geoserver/wfs',{
  type: 'GET',
  data: {
    service: 'WFS',
    version: '1.1.1',
    request: 'GetFeature',
    typename: 'geoportal:geo_app_counties',
    // CQL_FILTER: "county='Siaya'",
    srsname: 'EPSG:4326',
    outputFormat: 'application/json',
    },
  // dataType: 'jsonp',
  // jsonpCallback:'callback:handleJson',
  // headers: {
  //   'Access-Control-Allow-Credentials' : true,
  //   'Access-Control-Allow-Origin':'*',
  //   'Access-Control-Allow-Methods':'GET',
  //   'Access-Control-Allow-Headers':'application/json',
  // },
  // jsonp:'format_options',
  success:function(result){
      L.geoJson(result, {
        onEachFeature: function(feature, layer) {
              // layer.bindPopup(`Name: ${feature.properties.county}`)
              featureNames = feature.properties.county;
           $('#counties_dropdown').append('<a class="collapse-item county_list" href="#">'+featureNames+'</a>');
        }
       
    });

      $(".county_list").click(function() {
        // console.log("county list")
       county_value = $(this).text();
      // console.log(val)
      get_county(county_value);
      });
  }
 });


var countiesStyle = {
    color: 'black',
    weight: 1
}
var countyLayer = L.geoJson(null, {
  style:countiesStyle,
  onEachFeature: function(feature, layer) {
        layer.bindPopup(`Name: ${feature.properties.county}`)
        // console.log(feature.properties.county)
      }
});
countyLayer.addTo(map)
// console.log(turkanaLayer)
var vecLayer = L.geoJson(null, {
  style:countiesStyle,
  onEachFeature: function(feature, layer) {
        // layer.bindPopup(`Name: ${feature.properties.county}`)
        counties_data = feature.properties.county;
        $("county_list").html(counties_data);
        // console.log(counties_data)
      }
});
// console.log(vecLayer)
function handleJson(data){

  vecLayer.addData(data);
  // countyList.addData(data);
}

function get_county(value){
   countyname = value;
  console.log("the value is "+countyname)
  // CQL_FILTER: "county='Siaya'",
  $.ajax('http://127.0.0.1:8090/geoserver/wfs',{
  type: 'GET',
  data: {
    service: 'WFS',
    version: '1.1.1',
    request: 'GetFeature',
    typename: 'geoportal:geo_app_counties',
    // CQL_FILTER: "county='Turkana'",
    srsname: 'EPSG:4326',
    outputFormat: 'application/json',
    },
  // dataType: 'jsonp',
  // jsonpCallback:'callback:handleCounty',
  // jsonp:'format_options',
  success:function(result){
    // console.log(result)
  
    
       single_county =  L.geoJson(result, {
          // style:countiesStyle,
          filter: function(feature, layer) {
         
            return (feature.properties.county === countyname);
          },
           onEachFeature: function(feature, layer) {
                  if(layer){
             map.removeLayer(layer)
              
              }
            layer.bindPopup(`Name: ${feature.properties.county}`)

          }
        });

       single_county.addTo(map)
        
      
        
        //  single_county.addData(result);
    
            //  single_county.clearLayers();
             
      
 
        // console.log(single_county)
  }
 });
}

function handleCounty(data){
  // console.log(data)
  // countyLayer.addData(data);
}

var map = L.map('map', {
    center: [1.2921, 36.8219],
    zoom: 6,
    layers: [osm_layer, srtm_layer, countyLayer]
});

var baseMaps = {
    "OpenStreetMap": osm_layer,
    // "OpenStreetMap.HOT": osmHOT
};
var overlayMaps = {
    "SRTM": srtm_layer,
    "Counties": vecLayer
};
var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map);



// const geometry = {
//   type: 'Polygon',
//   coordinates: [
//     [
//       [125.90806629, 46.83817821],
//       [125.89487407, 46.82173077],
//       [125.91543337, 46.80596864],
//       [125.97282808, 46.79757359],
//       [125.9829364, 46.82532865],
//       [125.90806629, 46.83817821],
//     ],
//   ],
// };

// clippedWMS('http://geoserversh.nydsju.com/geoserver/sample/wms', {
//   layers: 'integration_space:growth_qinggang_202208',
//   format: 'image/png',
//   transparent: true,
//   version: '1.1.0',
//   crs: L.CRS.EPSG4326,
//   clip: geometry, // 唯一额外添加的参数
// }).addTo(this.map);



//  // Add WMS layer
//         var wmsLayer = L.tileLayer.wms('http://your-geoserver-url.com/geoserver/your-wms-layer', {
//             layers: 'your-wms-layer-name',
//             format: 'image/png',
//             transparent: true
//         }).addTo(map);

//         // Add WFS layer
//         var wfsLayer = L.geoJSON.ajax('http://your-geoserver-url.com/geoserver/your-wfs-layer', {
//             style: function (feature) {
//                 return {
//                     fillColor: 'transparent',
//                     weight: 1,
//                     opacity: 1,
//                     color: 'blue',
//                     fillOpacity: 0.7
//                 };
//             }
//         }).addTo(map);

//         // Clip WMS against WFS
//         wfsLayer.on('data:loaded', function () {
//             var wfsFeatures = wfsLayer.toGeoJSON();
//             var clippedFeatures = [];
//             wfsFeatures.features.forEach(function (feature) {
//                 var clipped = turf.intersect(wmsLayer.getBounds(), feature.geometry);
//                 if (clipped) {
//                     clippedFeatures.push(clipped);
//                 }
//             });
//             var clippedLayer = L.geoJSON(clippedFeatures).addTo(map);
//             wmsLayer.setClip(clippedLayer);
//         });