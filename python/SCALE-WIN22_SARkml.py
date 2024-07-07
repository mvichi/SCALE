#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:32:53 2024
Generate KML for SAR images
@author: vichi
"""

import simplekml 

#%% Generate KML file
DIR = ''
kml = simplekml.Kml()
kml.document.name = 'SCALE-WIN22-SAR'

#%% list of dictionaries contaning the TSX images
fol_TSX = kml.newfolder(name="TerraSARx")
tsx = [
{'name':'TSX1_20220714T1941',
 'begin':'2022-07-14',
 'file':['TerraSARx_images/TSX1_SAR__MGD_RE___SC_S_SRA_20220714T194156_20220714T194221_EPSG4326_QL_KMZ.png'],
 'coords':[[(-6.430823,-60.760514),(-1.864398,-60.760514),
           (-1.864398,-58.558039),(-6.430823,-58.558039)]]
 },

{'name':'TDX1_20220715T1924-StripMap',
 'begin':'2022-07-15',
 'file':['TerraSARx_images/TDX1_SAR__MGD_SE___SM_S_SRA_20220715T192432_20220715T192440_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TDX1_SAR__MGD_SE___SM_S_SRA_20220715T192439_20220715T192447_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TDX1_SAR__MGD_SE___SM_S_SRA_20220715T192447_20220715T192455_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TDX1_SAR__MGD_SE___SM_S_SRA_20220715T192455_20220715T192502_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TDX1_SAR__MGD_SE___SM_S_SRA_20220715T192502_20220715T192510_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TDX1_SAR__MGD_SE___SM_S_SRA_20220715T192510_20220715T192518_EPSG4326_QL_KMZ.png'
         ],
 'coords':[
           [(0.730675,-60.99360099999999),(1.700368,-60.99360099999999),
            (1.700368,-60.416714),(0.730675,-60.416714)],
           [(0.340413,-60.55531400000001),(1.293113,-60.55531400000001),
            (1.293113,-59.978794),(0.340413,-59.978794)],
           [(-0.046884,-60.107723),(0.8890570000000001,-60.107723),
             (0.8890570000000001,-59.531573),(-0.046884,-59.531573)],
           [(-0.4369170000000001,-59.6618),(0.495442,-59.6618),
             (0.495442,-59.083222),(-0.4369170000000001,-59.083222)],
           [(-0.804674,-59.211939),(0.09181700000000001,-59.211939),
            (0.09181700000000001,-58.638256),(-0.804674,-58.638256)],
           [(-1.163353,-58.761057),(-0.28194,-58.761057),
            (-0.28194,-58.187674),(-1.163353,-58.187674)]
           ]
 },
 
{'name':'TDX1_20220716T1907',
 'begin':'2022-07-16',
 'file':['TerraSARx_images/TDX1_SAR__MGD_RE___SC_S_SRA_20220716T190807_20220716T190832_EPSG4326_QL_KMZ.png'],
 'coords':[[(-2.667794,-59.014271),(2.760468,-59.014271),
           (2.760468,-56.63311900000001),(-2.667794,-56.63311900000001)]
           ]
 },
    
{'name':'TSX1_20220720T1933',
 'begin':'2022-07-20',
 'file':['TerraSARx_images/TSX1_SAR__MGD_RE___SC_S_SRA_20220720T193306_20220720T193335_EPSG4326_QL_KMZ.png'],
 'coords':[[(-3.84668,-61.516992),(1.023642,-61.516992),
           (1.023642,-59.080032),(-3.84668,-59.080032)]
           ]
 },

{'name':'TSX1_20220721T0447-StripMap',
 'begin':'2022-07-21',
 'file':['TerraSARx_images/TSX1_SAR__MGD_SE___SM_S_SRA_20220721T044710_20220721T044717_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TSX1_SAR__MGD_SE___SM_S_SRA_20220721T044717_20220721T044723_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TSX1_SAR__MGD_SE___SM_S_SRA_20220721T044723_20220721T044730_EPSG4326_QL_KMZ.png',
         'TerraSARx_images/TSX1_SAR__MGD_SE___SM_S_SRA_20220721T044730_20220721T044736_EPSG4326_QL_KMZ.png'
     ],
 'coords':[[(-0.862946,-58.35312399999999),(-0.05488100000000001,-58.35312399999999),
            (-0.05488100000000001,-57.850395),(-0.862946,-57.850395)],
           [(-1.155279,-58.730018),(-0.336302,-58.730018),
            (-0.336302,-58.226839),(-1.155279,-58.226839)],
           [(-1.460438,-59.11455099999999),(-0.62987,-59.11455099999999),
            (-0.62987,-58.610916),(-1.460438,-58.610916)],
           [(-1.772161,-59.498396),(-0.929739,-59.498396),
            (-0.929739,-58.994299),(-1.772161,-58.994299)]
           ]
 },
    
{'name':'TSX1_20220721T1916',
 'begin':'2022-07-21',
 'file':['TerraSARx_images/TSX1_SAR__MGD_RE___SC_S_SRA_20220721T191628_20220721T191650_EPSG4326_QL_KMZ.png'],
 'coords':[[(-2.217305,-59.626609),(0.481039,-59.626609),
           (0.481039,-57.967833),(-2.217305,-57.967833)]
           ]
 }

]

#%% CSK 
fol_CSK = kml.newfolder(name="Cosmo SkyMed SAR")
csk = [
{'name':'CSK_20220721T1736',
  'begin':'2022-07-21',
  'file':'CSK_images/CSK_202207211736.png',
  'north':-58.41954455538175,
  'south':-59.52267572428052,
  'east':0.6423025678704142,
  'west':-2.156398699803955
  }, 
{'name':'CSK_20220722T0702',
  'begin':'2022-07-22',
  'file':'CSK_images/CSK_202207220702.png',
 'north':-57.96073298324851, 
 'south':-59.45359823816254, 
 'east':1.893247356767542, 
 'west':-1.491065644624343
  }, 
{'name':'CSK_20220723T0720',
  'begin':'2022-07-23',
  'file':'CSK_images/CSK_202207230720.png',
 'north':-58.5483087963267, 
 'south':-60.02621710176014, 
 'east':-0.08252666663084884, 
 'west':-3.35203497471226
  }, 
{'name':'CSK_20220723T1635',
  'begin':'2022-07-23',
  'file':'CSK_images/CSK_202207231635.png',
 'north':-58.07160111405617, 
 'south':-59.47746453370322, 
 'east':0.9816422836974352, 
 'west':-2.309784917316492
  },
{'name':'CSK_20220724T0708',
  'begin':'2022-07-24',
  'file':'CSK_images/CSK_202207240708.png',
 'north':-58.36417994826953, 
 'south':-59.85825792881712, 
 'east':0.7196463432704894, 
 'west':-2.70670781341819
  },
{'name':'CSK_20220724T1617',
  'begin':'2022-07-24',
  'file':'CSK_images/CSK_202207241617.png',
 'north':-58.4069297180352, 
 'south':-59.88214307761628, 
 'east':1.744272009034147, 
 'west':-1.510144602274056
  },
{'name':'CSK_20220725T0708',
  'begin':'2022-07-25',
  'file':'CSK_images/CSK_202207250708.png',
 'north':-57.42037206702465, 
 'south':-58.90582622084469, 
 'east':-0.08959033247783843, 
 'west':-3.417309470970194
  },
{'name':'CSK_20220728T0702',
  'begin':'2022-07-28',
  'file':'CSK_images/CSK_202207280702.png',
 'north':-58.20248626000765, 
 'south':-59.610595467865, 
 'east':0.68630227359666, 
 'west':-2.622192917815538
  },
{'name':'CSK_20220728T1553',
  'begin':'2022-07-28',
  'file':'CSK_images/CSK_202207281553.png',
 'north':-58.08629935011916, 
 'south':-59.50060693343693, 
 'east':0.6371632038327015, 
 'west':-2.110603587232091
  }
]

#%% add the overlays and save
for sar in tsx:
    fg = fol_TSX.newfolder(name=sar['name'])
    fg.timespan.begin = sar['begin']
    fg.timespan.end = sar['begin']+'T23:59'
    for g in range(len(sar['file'])):
        ground = fg.newgroundoverlay(name='TSX image {}'.format(g))
        ground.icon.href = sar['file'][g]
        ground.gxlatlonquad.coords = sar['coords'][g]
        ground.style.balloonstyle.text = 'TerraSAR-x: '+sar['name']
        ground.style.balloonstyle.bgcolor = simplekml.Color.lightgreen
        ground.style.balloonstyle.textcolor = simplekml.Color.blue

for sar in csk:
    fg = fol_CSK.newfolder(name=sar['name'])
    fg.timespan.begin = sar['begin']
    fg.timespan.end = sar['begin']+'T23:59'
    ground = fg.newgroundoverlay(name='CSK image')
    ground.icon.href = sar['file']
    ground.latlonbox.north = sar['north']
    ground.latlonbox.south = sar['south']
    ground.latlonbox.east = sar['east']
    ground.latlonbox.west = sar['west']
    ground.style.balloonstyle.text = 'Cosmo SkyMed: '+sar['name']
    ground.style.balloonstyle.bgcolor = simplekml.Color.lightyellow
    ground.style.balloonstyle.textcolor = simplekml.Color.blue


kml.save(DIR+'../kml/SCALE-WIN22-SAR.kml')