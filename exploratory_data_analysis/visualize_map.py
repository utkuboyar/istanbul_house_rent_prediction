import pandas as pd
import numpy as np
import plotly.express as px
import pickle as _pickle


with open('regular_data', 'rb') as f:
    df = _pickle.load(f)
print(df.head())

'''
fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='rent',
                        mapbox_style="stamen-terrain")
 
fig.show()

'''

import plotly.express as px
fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="rent",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")
fig.show()