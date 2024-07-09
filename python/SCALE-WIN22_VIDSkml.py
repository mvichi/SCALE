#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:16:02 2024
Create KML file with youtube links to Giulio Passerotti's videos'
@author: vichi
"""

import simplekml 
import pandas as pd

#%% 
DS = 73 # seconds of movie per hour real-time
begin = ['2022-07-19 06:43:21','2022-07-20 14:50:00',
         '2022-07-21 08:53:36','2022-07-21 22:00:00',
         '2022-07-22 22:00:00','2022-07-23 22:00:00']
end = ['2022-07-19 16:16:30','2022-07-20 20:57:51',
         '2022-07-21 21:59:59','2022-07-22 21:59:59',
         '2022-07-23 21:59:59','2022-07-24 16:30:00']

duration = [641,441,
            917,1705,
            1711,1331] # seconds
start = [0,10,
         0,0,
         0,0] # seconds
links = ['https://youtu.be/By7bqU9kLj0',
         'https://youtu.be/99kqujHveJU',
         'https://youtu.be/qcYxVmzU_jY',
         'https://youtu.be/oIuuyWDEQjU',
         'https://youtu.be/jG5n_TukoN8',
         'https://youtu.be/yIUkXXzrxRA'
         ]

#%% load ship track
sds = pd.read_csv('../data/track/SCALE-WIN22-SDS_1min.csv',
                    index_col=1,parse_dates=True)


#%% Write KML file
kml = simplekml.Kml()
name = 'SCALE-WIN22-VIDS'
kml.document.name = name

fol = kml.newfolder(name="Port Camera Footages")

style = simplekml.Style()
style.labelstyle.scale = 0.5  # Text 
style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pal2/icon22.png'
style.iconstyle.scale = 0.8 

for i in range(len(links)):
    # extract hourly intervals and creat the url to the youtube video
    frames = pd.date_range(begin[i],end[i],freq='1H')
    url = [links[i]+'?t={}'.format(start[i]+DS*t) for t in range(len(frames)-1)]
    # get corresponding locations
    idx = sds.index.get_indexer(frames[:-1], method='nearest')
    i_sds = sds.iloc[idx]
    for p in range(len(url)):
        pnt = fol.newpoint(coords=[(i_sds['LON_DEC'][p],
                              i_sds['LAT_DEC'][p])],
                         name=i_sds.index[p].strftime('%m/%dT%H:%M'))
        pnt.description = '<a href="{}">{}</a>'.format(url[p],url[p])
        pnt.style = style


kml.save('../kml/{}.kml'.format(name))


