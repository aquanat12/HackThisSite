import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
from matplotlib.patches import Arc
from matplotlib import patches
import pandas as pd
from tkinter import *

XEndList = []
YEndList = []
XStartList = []
YStartList = []
LColorList = []
RadiusList = []
YCenterList = []
ArcExtendList = []
RColorList = []
ArcStartList = []
XCenterList = []


plotMe = ET.parse('PlotMe.xml')
root = plotMe.getroot()
Line = root.findall('Line')
Arc = root.findall('Arc')


for a in Line:
    XEnd = a.find('XEnd')
    XEndList.append(XEnd.text)
    YEnd = a.find('YEnd')
    YEndList.append(YEnd.text)
    XStart = a.find('XStart')
    XStartList.append(XStart.text)
    YStart = a.find('YStart')
    YStartList.append(YStart.text)
    LColor = a.find('Color')
    if LColor is None:
        LColorList.append("white")
    else:
        LColorList.append(LColor.text)

for b in Arc:
    Radius = b.find('Radius')
    RadiusList.append(Radius.text)
    YCenter = b.find('YCenter')
    YCenterList.append(YCenter.text)
    ArcExtend = b.find('ArcExtend')
    ArcExtendList.append(ArcExtend.text)
    ArcStart = b.find('ArcStart')
    ArcStartList.append(ArcExtend.text)
    XCenter = b.find('XCenter')
    XCenterList.append(XCenter.text)
    RColor = b.find('Color')
    if RColor is None:
        RColorList.append("white")
    else:
        RColorList.append(RColor.text)


LineData = {'XEnd':  XEndList,
            'YEnd': YEndList,
            'XStart': XStartList,
            'YStart': YStartList,
            'LColor': LColorList
            }

linedf = pd.DataFrame (LineData, columns = ['XEnd', 'YEnd' , 'XStart', 'YStart', 'LColor'])
linedf = linedf.astype({'XEnd': 'float', 'YEnd': 'float', 'XStart': 'float', 'YStart': 'float', 'LColor': 'object'})


ArcData = {'Radius':  RadiusList,
           'YCenter': YCenterList,
           'ArcExtend': ArcExtendList,
           'ArcStart': ArcStartList,
           'XCenter': XCenterList,
           'RColor': RColorList
           }

arcdf = pd.DataFrame (ArcData, columns = ['Radius', 'YCenter', 'ArcExtend', 'ArcStart', 'XCenter', 'RColor'])
arcdf = arcdf.astype({'Radius': 'float', 'YCenter': 'float', 'ArcExtend': 'float', 'ArcStart': 'float', 'XCenter': 'float', 'RColor': 'object'})

    
    
window = Tk()
canvas = Canvas(window, width=800, height=800, background='black')
canvas.grid(row=0,column=0)
for i in range(len(linedf)):
    canvas.create_line([linedf.iloc[i]['XStart'],(800 - linedf.iloc[i]['YStart'])], [linedf.iloc[i]['XEnd'],(800 - linedf.iloc[i]['YEnd'])], fill=linedf.iloc[i]['LColor'])
for j in range(len(arcdf)):
    canvas.create_arc(arcdf.iloc[j]['XCenter'],(800 - (arcdf.iloc[j]['YCenter'] + arcdf.iloc[j]['Radius'])),(arcdf.iloc[j]['XCenter'] + arcdf.iloc[j]['Radius']),(800 - arcdf.iloc[j]['YCenter']), start=(90 - arcdf.iloc[j]['ArcStart']), extent=arcdf.iloc[j]['ArcExtend'], outline=arcdf.iloc[j]['RColor'], style=ARC)
    canvas.pack()
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

#window.bind('<Motion>', motion)
window.mainloop()
