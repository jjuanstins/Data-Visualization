#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:16:55 2019

@author: roshanahmed
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

def argParser():
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--outputfile','-o',type=str, help='specify filename of your outputfile')
        return vars(parser.parse_args())
    
plt.style.use('BME163.mplstyle')
      
args=argParser()
fileName=args['outputfile']

x_values = []
y_values = []

for line in open("BME163_Input_Data_1.txt"):
    a =line.strip().split('\t')
    number1 = int(a[1])
    number2 = int(a[2])
    
    x_values.append(number1)
    y_values.append(number2)

x_array = np.asarray(x_values)
y_array = np.asarray(y_values)
x_log = np.log2(x_array + 1)
y_log = np.log2(y_array + 1)
x_list = np.array(x_log).tolist()
y_list = np.array(y_log).tolist()


figure_width = 5
figure_height = 2

plt.figure(figsize=(figure_width,figure_height))
panel_width = 1/figure_width
panel_height = 1/figure_height

panel1 = plt.axes([0.14,0.15,panel_width,panel_height])
panel1.set_xlim(0,15)
panel1.set_ylim(0,15)
plt.yticks([], [])
panel1.scatter(x_list, y_list,
               s = 2,
               facecolor = 'black',
               linewidth = 0,
               alpha=0.1)


panel2_width = 0.25/figure_width
panel2_height = 0.25/figure_height
panel2 = plt.axes([0.076,0.15,panel2_width,panel_height])
panel2.set_xlim(20,0)
panel2.set_ylim(0,15)

panel3 = plt.axes([0.14,0.685,panel_width,panel2_height])
panel3.set_xlim(0,15)
panel3.set_ylim(0,20)
panel3.set_xticks([])

panel4 = plt.axes([0.476,0.15,panel2_width,panel_height])
panel4.set_xlim(20,0)
panel4.set_ylim(0,15)

panel5 = plt.axes([0.54,0.15,panel_width,panel_height])
panel5.set_xlim(0,15)
panel5.set_ylim(0,15)
panel5.set_yticks([])

panel6 = plt.axes([0.54,0.685,panel_width,panel2_height])
panel6.set_xlim(0,15)
panel6.set_ylim(0,20)
panel6.set_xticks([])


bins = np.linspace(0,14,29)

x_histogram, bins = np.histogram(x_list,bins)
for index in range(0,len(x_histogram),1):
    bottom = 0
    left = bins[index]
    width = bins[index + 1] - left
    height = np.log2(x_histogram[index] + 1)
    rectangle1 = mplpatches.Rectangle([left,bottom],width,height,
                                     edgecolor='black',
                                     facecolor='grey',
                                     linewidth=0.1)
    panel3.add_patch(rectangle1)
    rectangle1 = mplpatches.Rectangle([left,bottom],width,height,
                                     edgecolor='black',
                                     facecolor='grey',
                                     linewidth=0.1)
    panel6.add_patch(rectangle1)

y_histogram, bins = np.histogram(y_list,bins)
for index in range(0,len(y_histogram),1):
    bottom = 0
    left=bins[index]
    width=bins[index + 1] - left
    height=np.log2(y_histogram[index] + 1)
    rectangle1=mplpatches.Rectangle([bottom,left],height,width,
                                    edgecolor='black',
                                    facecolor='grey',
                                    linewidth=0.1 )
    panel2.add_patch(rectangle1)
    rectangle1=mplpatches.Rectangle([bottom,left],height,width,
                                    edgecolor='black',
                                    facecolor='grey',
                                    linewidth=0.1 )
    panel4.add_patch(rectangle1)



"""
Extra Credit
"""
panel7 = plt.axes([0.8,0.15,(.1/figure_width), panel_height])
panel7.set_xticks([])
panel7.set_yticks([0,10,20])
panel7.set_yticklabels(["0", "10", ">20"])


panel5.scatter(x_list, y_list,
               s = 1.25,
               marker = 's',
               facecolor = 'black',
               linewidth = 0,
               alpha=0.1)


for x_index in range(0,10,10):
    for y_index in range(0,20,1):
        color = 1 - y_index/20
        rectangle2 = mplpatches.Rectangle([x_index, y_index],1,1,
                                          edgecolor = "black",
                                          facecolor = (color, color, color),
                                          linewidth = 0)
        panel7.add_patch(rectangle2)
                                          
                                          
plt.savefig('Ahmed_Roshan_BME163_Assigmnment_Week2.png',dpi=600)














