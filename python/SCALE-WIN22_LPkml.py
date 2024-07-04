#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 08:03:48 2024

Generate KML file for LainePoiss buoy data

@author: vichi
"""

import pandas as pd
import simplekml 
import numpy as np
#%% Import data
DIR = ''
LP = []
LPname = ['LP2','LP4','LP8']

# buoy tracks
for b in LPname:
    lp = pd.read_csv(DIR+'../data/track/{}.csv'.format(b),
                    index_col=0,parse_dates=True)
    LP.append(lp)

#%% Generate KML file

kml = simplekml.Kml()
kml.document.name = 'SCALE-WIN22-LP'
fol_lp = kml.newfolder(name="LainePoiss buoys")


#%% Add the map elements
# Create styles for buoys
buoy_style = []
for icon in ['ltblu-circle','ltblu-stars','ltblu-square']:
    style = simplekml.Style()
    style.labelstyle.scale = 0.7  # Text 
    style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/{}.png'.format(icon)
    style.iconstyle.scale = 1  # Icon scale
    #style.iconstyle.color = simplekml.Color.aliceblue
    buoy_style.append(style)

# Create syle for buoy tracks
track_style = simplekml.Style()
track_style.linestyle.color = simplekml.Color.aquamarine
    
for b in range(len(LP)):
    buoy = LP[b]
    # convert the timestamps to the right format for kml
    ts_buoy = buoy.index.strftime('%Y-%m-%dT%H:%M')   
    fol_buoy = fol_lp.newfolder(name=LPname[b])
    for i in range(len(buoy)):
        pnt = fol_buoy.newpoint(coords=[(buoy['Longitude'][i],
                                         buoy['Latitude'][i])],
                                 )
        pnt.timestamp.when = ts_buoy[i]
        pnt.style = buoy_style[b] 
        pnt.extendeddata.newdata(name='Name', 
                                 value=LPname[b])
        pnt.extendeddata.newdata(name='Datetime',
                                 value=ts_buoy[i])
    fol_track = fol_lp.newfolder(name=LPname[b]+'_track')
    for i in range(1,len(buoy)):
        line=fol_track.newlinestring(coords=[(buoy['Longitude'][i-1],
                                         buoy['Latitude'][i-1]),
                                       (buoy['Longitude'][i],
                                        buoy['Latitude'][i])])
        line.timestamp.when = ts_buoy[i-1]
        line.style = track_style

kml.save(DIR+'../kml/SCALE-WIN22-LP.kml')