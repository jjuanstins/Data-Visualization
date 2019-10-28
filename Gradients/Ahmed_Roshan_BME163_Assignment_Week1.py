#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:14:31 2019

@author: roshanahmed

Lab1 BME163
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

def argParser():
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--outputfile','-o',type=str, help='specify filename of your outputfile')
        return vars(parser.parse_args())
      
args=argParser()
fileName=args['outputfile']
plt.style.use('BME163.mplstyle')

figure_width = 3.42
figure_height = 2

plt.figure(figsize=(figure_width,figure_height))
panel_width=1/figure_width
panel_height=1/figure_height

panel1=plt.axes([0.1,0.2,panel_width,panel_height])
plt.xticks([], [])
plt.yticks([], [])


for index in np.linspace(0, np.pi/2, 25):
    x = np.cos(index)
    y = np.sin(index)
    panel1.plot(x,y,
                color='black',
                marker='o',
                markeredgewidth=0,
                markerfacecolor= (x ,x,x),
                markersize=2,
                linewidth=0)

    
panel2=plt.axes([0.55,0.2,panel_width,panel_height])
plt.xticks([], [])
plt.yticks([], [])


for horizontal_index in range(0,10,1):
    for vertical_index in range(0,10,1):
        rectangle1=mplpatches.Rectangle([horizontal_index,vertical_index],1,1,
                                    edgecolor = 'black',
                                    facecolor = (horizontal_index/10, vertical_index/10, 1),
                                    linewidth = 1)
        
        panel2.add_patch(rectangle1)
        
        
panel2.set_xlim(0,10)
panel2.set_ylim(0,10)

plt.savefig('fileNamw',dpi=600)

