#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 08:03:48 2024

Generate KML file for SHARC buoy data

@author: vichi
"""

import pandas as pd
import simplekml 
import numpy as np
#%% Import data
DIR = ''
# buoy tracks
sdf = pd.read_csv(DIR+'../data/track/SCALE-WIN22-SHARC.csv',
                    index_col=0,parse_dates=True)
# replace 0 with missing values
sdf = sdf.replace([0],np.nan)
sdf.dropna(subset=['GPS Latitude'], inplace=True)
SB = np.sort(sdf['Device Name'].unique())



#%% Generate KML file

kml = simplekml.Kml()
kml.document.name = 'SCALE-WIN22-SHARC'
fol_sharc = kml.newfolder(name="SHARC buoys")


#%% Create styles for buoys
colors = ['FFFFFFAA', 'FFF08C14', 'FFFF78F0', 'FF1478C8', 'FF1478FF', 'FFC8C8C8']
buoy_style = []
for b in range(len(SB)):
    style = simplekml.Style()
    style.labelstyle.scale = 0.7  # Text 
    style.iconstyle.color = colors[b]  # Red
    style.iconstyle.scale = 1  # Icon
    buoy_style.append(style)
    
for b in range(len(SB)):
    buoy = sdf[sdf['Device Name'] == SB[b]]
    # convert the timestamps to the right format for kml
    ts_buoy = buoy.index.strftime('%Y-%m-%dT%H:%M')   
    fol_buoy = fol_sharc.newfolder(name=SB[b])
    for i in range(len(buoy)):
        pnt = fol_buoy.newpoint(coords=[(buoy['GPS Longitude'][i],
                                         buoy['GPS Latitude'][i])],
                                 name=SB[b])
        pnt.timestamp.when = ts_buoy[i]
        pnt.style = buoy_style[b] 
        pnt.extendeddata.newdata(name='Datetime',
                                 value=ts_buoy[i])

kml.save(DIR+'../kml/SCALE-WIN22-SHARC.kml')