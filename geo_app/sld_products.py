sld_products = {
  "Exposure":{
    "Land Cover":{
        "sld_rule":"""<sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
                <sld:ContrastEnhancement>
                  <sld:GammaValue>1.0</sld:GammaValue>
                </sld:ContrastEnhancement>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="values">
               <sld:ColorMapEntry color="#ffffff" opacity="0.0" quantity="0" label="No Data"/>
              <sld:ColorMapEntry color="#a7a800" opacity="1.0" quantity="1" label="Agriculture"/>
              <sld:ColorMapEntry color="#2d8310" opacity="1.0" quantity="2" label="Forest"/>
              <sld:ColorMapEntry color="#ffebbe" opacity="1.0" quantity="3" label="Grassland"/>
              <sld:ColorMapEntry color="#277f8e" opacity="1.0" quantity="4" label="Wetland"/>
              <sld:ColorMapEntry color="#a60601" opacity="1.0" quantity="5" label="Artificial"/>
              <sld:ColorMapEntry color="#5bfa04" opacity="1.0" quantity="6" label="Shrubland"/>
              <sld:ColorMapEntry color="#cccccc" opacity="1.0" quantity="7" label="Bare"/>
              <sld:ColorMapEntry color="#02c5ff" opacity="1.0" quantity="8" label="Water"/>
            </sld:ColorMap>
            <sld:ContrastEnhancement/>
          </sld:RasterSymbolizer>
        </sld:Rule>"""
    }
  }
}


"""format for sld, building the format"""

sld_start = """<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>land_cover</sld:Name>
    <sld:UserStyle>
      <sld:Name>land_cover</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Name>name</sld:Name>
        <Transformation>
  <ogc:Function name="gs:CropCoverage">
        <ogc:Function name="parameter">
          <ogc:Literal>coverage</ogc:Literal>
        </ogc:Function>
        <ogc:Function name="parameter">
          <ogc:Literal>cropShape</ogc:Literal>
          <ogc:Literal>"""

sld_middle = """</ogc:Literal>
        </ogc:Function>
  </ogc:Function>
  </Transformation>"""
sld_end = """</sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>"""

