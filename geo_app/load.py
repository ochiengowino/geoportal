from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Counties



# Auto-generated `LayerMapping` dictionary for Counties model
counties_mapping = {
    'county': 'COUNTY',
    'total_pop': 'Total_Pop',
    'covidcases': 'CovidCases',
    'geom': 'MULTIPOLYGON',
}
# counties_shp1 = Path(__file__).resolve().parent / "data" / "counties_shp"/ "County.shp"

counties_shp = Path(__file__).resolve().parent / "data" / "County.shp"

def run(verbose=True):
    lm = LayerMapping(Counties, counties_shp, counties_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)