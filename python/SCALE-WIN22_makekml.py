#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 05:51:07 2022

SCALE-WIN22 reporting
Creates the kml file of tracks and SAR images

@author: vichi
"""

import pandas as pd
import simplekml 
#%% Import data
DIR = ''
# ship track
sds = pd.read_csv(DIR+'../data/track/SCALE-WIN22-SDS_1min.csv',
                    index_col=1,parse_dates=True)
# station data
stations = pd.read_csv(DIR+'../data/track/SCALE-WIN22-stations.csv',
                    index_col=4,parse_dates=True)
#%% export kml


kml = simplekml.Kml()

kml.document.name = 'SCALE-WIN22'

# style to be used for stations
stations_style = simplekml.Style()
stations_style.labelstyle.scale = 1  # Text 
stations_style.iconstyle.color = simplekml.Color.red
stations_style.iconstyle.scale = 1  # Icon

# style for ship track
track_style = simplekml.Style()
track_style.linestyle.color = simplekml.Color.whitesmoke
track_style.linestyle.scale = 1.5

# overlay SCALE logo
screen = kml.newscreenoverlay(name='SCALE logo')
screen.icon.href = 'SCALE-WIN22_logo.png'
screen.overlayxy = simplekml.OverlayXY(x=0,y=1,xunits=simplekml.Units.fraction,
                                       yunits=simplekml.Units.fraction)
screen.screenxy = simplekml.ScreenXY(x=0,y=1,xunits=simplekml.Units.fraction,
                                     yunits=simplekml.Units.fraction)

# add stations and track
fol_stations = kml.newfolder(name="Stations")
fol_track = kml.newfolder(name="Track")
# convert the timestamps to the right format for kml
ts_stations = stations.index.strftime('%Y-%m-%dT%H:%M')
ts_track = sds.index.strftime('%Y-%m-%dT%H:%M')
for i in range(len(stations)):
    pnt=fol_stations.newpoint(coords=[(stations['LON_DEC_OPEN'][i],
                              stations['LAT_DEC_OPEN'][i])],
                     name=stations['NAME'][i])
    pnt.timestamp.when = ts_stations[i]
    pnt.style = stations_style
    pnt.extendeddata.newdata(name='DATETIME_OPEN_UTC',
                             value=stations.index[i].strftime('%Y/%m/%d %H:%M'))
    pnt.extendeddata.newdata(name='DATETIME_CLOSED_UTC',
                             value=stations.DATETIME_CLOSED_UTC[i])
    pnt.extendeddata.newdata(name='SOUNDING',
                             value=str(stations.SOUNDING[i])+' m')
    pnt.extendeddata.newdata(name='ACTIVITIES',value=stations.ACTIVITIES[i])

for i in range(1,len(sds)-1):
    line=fol_track.newlinestring(coords=[(sds['LON_DEC'][i-1],
                                    sds['LAT_DEC'][i-1]),
                                   (sds['LON_DEC'][i],
                                    sds['LAT_DEC'][i])])
    line.timestamp.when = ts_track[i-1]
    line.style = track_style

# add placemarks for CSK SAR images
CSK_time = [
    '2022-07-21T17:36',
    '2022-07-22T07:02',
    '2022-07-23T07:20',
    '2022-07-23T16:35',
    '2022-07-24T07:08',
    '2022-07-24T16:17',
    '2022-07-25T07:08',
    '2022-07-28T07:02',
    '2022-07-28T15:53'    
    ]
fol_CSK = kml.newfolder(name='CSK SAR location')
for i in range(len(CSK_time)):
    p = sds.loc[CSK_time[i]]
    pnt = fol_CSK.newpoint(coords=[(p.LON_DEC, p.LAT_DEC)],
                           name='CSK'+CSK_time[i])
    pnt.iconstyle.color = simplekml.Color.yellow
    pnt.labelstyle.scale = 0.7  # Text
    pnt.timestamp.when = CSK_time[i]
    pnt.extendeddata.newdata(name='DATE',value=CSK_time[i])
    pnt.extendeddata.newdata(name='Description',
                             value='Ship location at time of Cosmo-Sky SAR acquisition')

# add placemarks for TSX SAR images (stripMaps are identified by the first strip)
TSX_time = [
    '2022-07-14T19:41',
    '2022-07-15T19:24',
    '2022-07-16T19:08',
    '2022-07-20T19:33',
    '2022-07-21T04:47',
    '2022-07-21T19:16'
    ]
fol_TSX = kml.newfolder(name='TSX SAR location')
for i in range(len(TSX_time)):
    p = sds.loc[TSX_time[i]]
    pnt = fol_TSX.newpoint(coords=[(p.LON_DEC, p.LAT_DEC)],
                           name='TSX'+TSX_time[i])
    pnt.iconstyle.color = simplekml.Color.green
    pnt.labelstyle.scale = 0.7  # Text
    pnt.timestamp.when = TSX_time[i]
    pnt.extendeddata.newdata(name='DATE',value=TSX_time[i])
    pnt.extendeddata.newdata(name='Description',
                             value='Ship location at time of Terrasar-X SAR acquisition')
    
kml.save(DIR+'../kml/SCALE-WIN22.kml')
