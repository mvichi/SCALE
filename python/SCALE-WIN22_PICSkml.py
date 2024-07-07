#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 19:27:36 2024

Create a kml with placemarks and pictures

@author: vichi
"""
import simplekml 
import pandas as pd
import os
from PIL import Image, ExifTags
from datetime import datetime

#%% Open

DIRIMG = '../data/images/aspect/'
pics = os.listdir(DIRIMG)

# ship track
sds = pd.read_csv('../data/track/SCALE-WIN22-SDS_1min.csv',
                    index_col=1,parse_dates=True)
#%% query the image exif and get the datetime
def get_exif_field (exif,field) :
    for (k,v) in exif.items():
        if ExifTags.TAGS.get(k) == field:
            return v
a_date = []
for p in pics:
    img = Image.open(DIRIMG+p)
    img_exif = img.getexif()
    date = get_exif_field(img_exif,'DateTime')
    a_date.append(datetime.strptime(date, '%Y:%m:%d %H:%M:%S'))
#%% Get the list of tags from an image
if img_exif is None:
    print('Sorry, image has no exif data.')
else:
    for key, val in img_exif.items():
        if key in ExifTags.TAGS:
            print(f'{ExifTags.TAGS[key]}:{val}')
        else:
            print(f'{key}:{val}')

#%% Find indices of pics dates on the ship track
a_idx = sds.index.get_indexer(pd.to_datetime(a_date), method='nearest')
a_sds = sds.iloc[a_idx]

#%% Write KML file
kml = simplekml.Kml()
kml.document.name = 'SCALE-WIN22-PICS'

fol_A = kml.newfolder(name="ASpeCT images")

style = simplekml.Style()
style.labelstyle.scale = 0.6  # Text 
style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/camera.png'
style.iconstyle.scale = 1 

for i,p in enumerate(pics):
    path = kml.addfile(DIRIMG+p)
    pnt = fol_A.newpoint(coords=[(a_sds['LON_DEC'][i],
                              a_sds['LAT_DEC'][i])],
                         name=a_sds.index[i].strftime('%m/%dT%H:%M'))
    pnt.description = '<img src=' + path +' alt=picture width=400 height=300 align=left />'
    pnt.style = style
    # pnt.extendeddata.newdata(name='DATETIME',
    #                          value=a_sds.index[i].strftime('%Y/%m/%dT%H:%M'))


kml.savekmz('../kml/SCALE-WIN22-PICS.kmz')