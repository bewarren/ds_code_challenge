<img src="img/city_emblem.png" alt="City Logo"/>

# City of Cape Town - Data Science Unit Code Challenge

### 2. Initial Data Transformation (if applying for a Data Engineering, Visualisation Engineer, Front End Developer and/or Science Position)

First make sure the relevant packages are installed, and that the data is in the relevant folders `data/sr.csv` and `data/city-hex-polygons-8.geojson`

```bash
pip install pandas geopandas shapely
```

Then run the code using:

```bash
python code/format_data.py
```

An error threshold of

```python
error_threshold = (df['latitude'].isna() | df['longitude'].isna() | df['official_suburb'].isna()).sum()
```

was chosen since if you don't have the latitude, longitude or official suburb then we can't map to a hex value. I tried with just longitude and latitude but this threshold was found to be too low such that it would always fail on the current data set but only by about 3 service requests.

To validate the output data run the below code making sure the validation data is in the correct path `data/sr_hex.csv`

```bash
python code/validate.py
```

### 6. Data Visualisation Task (if applying for a Data Visualisation Engineering or Front End Developer Position)

I build the visualisations using NextJS, the Recharts Library, and MapBox. And the code is hosted on Vercel

The visualisation is hosted at [City of CT Data Visualisation](https://data-visualisation-r61m4677q-bewarren.vercel.app) and my code sits in a separate repositiory [Here](https://github.com/bewarren/data-visualisation)

The data was generated with the `code/convert_data_for_map.py` and `code/convert_data_for_vis.py` files and the text files were copied into ts files to display on the maps.

The requested markdown files sit at `markdown/data-driven-storytelling.md` and `markdown/visualisation-design-choices.md`
