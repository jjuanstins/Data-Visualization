#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:50:01 2019

@author: roshanahmed
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mplpatches
import argparse


def argParser():
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--outputfile','-o',type=str, help='specify filename of your outputfile')
        parser.add_argument('--inputfile','-i',type=str, help='specify filename of your input')
        return vars(parser.parse_args())
    
args=argParser()
fileIn=args['inputfile']
fileName=args['outputfile']
plt.style.use('BME163.mplstyle')

figure_width = 5
figure_height = 3

plt.figure(figsize=(figure_width,figure_height))

panel1 = plt.axes([0.1, 0.1, 0.75/figure_width ,2.5/figure_height]) 

panel1.set_xlim([0, 16])
panel1.set_ylim([0, 1265])
panel1.set_xticks([1,3,5,7,9,11,13,15])
panel1.set_xticklabels([0,'',6,'',12,'',18,''])
panel1.set_yticks([0,200,400,600,800,1000,1200])
panel1.set_xlabel("CT")
panel1.set_ylabel("Number of genes")

panel2 = plt.axes([.35, 0.1, 2.5/figure_width, 2.5/figure_height], frameon=False)
panel2.set_ylim(-400,400)
panel2.set_xlim(-400,400)
panel2.set_xticks([])
panel2.set_yticks([])
panel2.text( 0,0, 'CT', ha = 'center', va = 'center', fontsize = 6, zorder=3)  
panel2.text( 0,50, '0', ha = 'center', va = 'center', fontsize = 6, zorder=3)
panel2.text( 43.5,25, '4', ha = 'center', va = 'center', fontsize = 6, zorder=3)
panel2.text( 43.5,-25, '8', ha = 'center', va = 'center', fontsize = 6, zorder=3)
panel2.text( 0,-50, '12', ha = 'center', va = 'center', fontsize = 6, zorder=3) 
panel2.text( -43.5,-25, '16', ha = 'center', va = 'center', fontsize = 6, zorder=3)
panel2.text( -43.5,25, '20', ha = 'center', va = 'center', fontsize = 6, zorder=3)
panel2.text( -200,0, '100', ha = 'right', va = 'center', fontsize = 6, zorder=3)
panel2.text( -300,0, '200', ha = 'right', va = 'center', fontsize = 6, zorder=3)
panel2.text( -400,0, '300', ha = 'right', va = 'center', fontsize = 6, zorder=3)

Yellow=(255,225,40)
Blue=(56,66,157)
R = np.linspace(Yellow[0]/255,Blue[0]/255,101)
G = np.linspace(Yellow[1]/255,Blue[1]/255,101)
B = np.linspace(Yellow[2]/255,Blue[2]/255,101)

FPKM = []
peak_phase = []

headLine = 0 
for line in open('BME163_Input_Data_4.txt'):
    if headLine is not 0:
        splitted = line.strip().split('\t')
        CT = float(splitted[13])
        FPKM.append([CT, \
                     int(splitted[4]), \
                     int(splitted[5]), \
                     int(splitted[6]), \
                     int(splitted[7]), \
                     int(splitted[8]), \
                     int(splitted[9]), \
                     int(splitted[10]), \
                     int(splitted[11])])
        peak_phase.append(CT)     
        
    elif headLine is 0:
        headLine = 1

FPKM.sort(reverse=True, key=lambda x: x[0])

y = 0  
for column in FPKM:
    row_list = np.array([column[1], column[2], column[3], column[4], column[5], column[6], column[7], column[8]])
    normalized_list = ((row_list - min(row_list)) / (max(row_list) - min(row_list))) * 100
    x = 0
    for position in normalized_list:
        color = (R[int(position)], G[int(position)], B[int(position)])
        rectangle = mplpatches.Rectangle([x, y], 3.571, 1,facecolor=color, linewidth=0)
        panel1.add_patch(rectangle)
        x += 2
    y += 1


"""
dashed outside circles
"""
for radius in [200, 300, 400]:
    x_list=[]
    y_list=[]
    for rad in np.linspace(0,np.pi*2,100):
        x = np.cos(rad) * radius
        y = np.sin(rad) * radius
        x_list.append(x)
        y_list.append(y)

    panel2.plot(x_list,y_list,
                zorder=3, 
                linestyle='--', 
                dashes = (11,6,6,6), 
                linewidth = 0.35, 
                color = 'black')
    
"""
colors half of inner circle
"""
for radius in range(80,100):
    x_list=[]
    y_list=[]
    for rad in np.linspace((np.pi/2), (3*np.pi /2), 100):
        x = np.cos(rad) * radius
        y = np.sin(rad) * radius
        x_list.append(x)
        y_list.append(y)

    panel2.plot(x_list,y_list,
                marker='o',
                mfc='black', 
                markersize=0, 
                zorder=1,
                linewidth = 0.25, 
                color = 'black')

"""
makes inner circles
"""
for radius in [80, 100]:
    x_list=[]
    y_list=[]
    for rad in np.linspace(0,np.pi*2,100):
        x = np.cos(rad) * radius
        y = np.sin(rad) * radius
        x_list.append(x)
        y_list.append(y)

    panel2.plot(x_list,y_list,
                marker='o', 
                mfc='black', 
                markersize=0,
                zorder=3, 
                linewidth = 0.25, 
                color = 'black')

"""
Covers middle 
"""
x_list=[]
y_list=[]
for radius in np.linspace(0, (2 * np.pi), 100):
    for rad in np.linspace(0,78, 100):
        x = np.cos(radius) * rad
        y = np.sin(radius) * rad
        x_list.append(x)
        y_list.append(y)

    panel2.plot(x_list,y_list,
                marker='o',
                markersize=0, 
                zorder=2,  
                linewidth=1, 
                color = 'white')


bins = np.arange(0,26,2)
histogram, bins = np.histogram(peak_phase,bins)
    
start = np.pi/2
end = np.pi/3
for steps in histogram:
    height = steps
    shade_x = []
    shade_y = []
    top_x = []
    top_y = []
    side_x = []
    side_y = []        
    side2_x = []
    side2_y = []

    for radian in np.linspace(start,end,1000):

        for radius in np.linspace(100, height + 100, height):
            x_pos=np.cos(radian)* radius
            y_pos=np.sin(radian)* radius
            shade_x.append(x_pos)
            shade_y.append(y_pos)
             
            
            if radius == (height + 100):
                x_t = np.cos(radian)* radius
                y_t = np.sin(radian)* radius
                top_x.append(x_t)
                top_y.append(y_t)
                
                
            elif radian == start:
                sidex = np.cos(radian)* radius 
                sidey = np.sin(radian)* radius
                side_x.append(sidex)  
                side_y.append(sidey)
                    
            elif radian == end :
                side2x = np.cos(radian)* radius
                side2y = np.sin(radian)* radius
                side2_x.append(side2x)
                side2_y.append(side2y)
                    
    panel2.plot(shade_x,shade_y,
                marker='o', 
                mfc='black', 
                markersize=0, 
                linewidth=0.5,
                color='grey')
    
    panel2.plot(top_x,top_y,
                marker='o', 
                mfc='black',
                markersize=0, 
                linewidth=0.4,
                color='black',
                zorder = 5)
    
    panel2.plot(side_x,side_y,
                marker='o', 
                mfc='black', 
                markersize=0, 
                linewidth=0.3,
                color='black', 
                zorder = 5)
         
    panel2.plot(side2_x,side2_y,
                marker='o', 
                mfc='black', 
                markersize=0, 
                linewidth=0.3,
                color='black', 
                zorder = 4)


    start -= (np.pi)/6
    end -= (np.pi)/6


plt.savefig('Ahmed_Roshan_BME163_Assignment_Week6',dpi=600)
