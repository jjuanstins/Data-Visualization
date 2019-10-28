#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:00:26 2019

@author: roshanahmed
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import argparse

def argParser():
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--outputfile','-o',type=str, help='specify filename of your outputfile')
        return vars(parser.parse_args())
    
plt.style.use('BME163.mplstyle')
      
args=argParser()
fileName=args['outputfile']

figure_width = 3
figure_height = 3

plt.figure(figsize=(figure_width,figure_height))
panel_width = 2/figure_width
panel_height = 2/figure_height

panel1 = plt.axes([0.165,0.165,panel_width,panel_height])
panel1.set_xlim(-12,12)
panel1.set_ylim(0,60)

#panel1.set_xticks([-10,-5,0,5,10])
#panel1.set_yticks([0,10,20,30,40,50,60])

panel1.set_xlabel('log' + '$_2$' + '(fold change)')
panel1.set_ylabel('-log' + '$_{10}$' + '(p-value)')
mpl.rcParams['mathtext.default'] = 'default'

black_x = []
black_y = []
red_x = []
red_y = []
label_x = []
label_y = []
labels = []

for line in open("BME163_Input_Data_2.txt"):
    a =line.strip().split('\t')
    label = (a[0])
    number1 = (a[1])
    number2 = (a[2])
    
    if number1 == 'NA' and number2 == 'NA':
        x = 1
        y = 0
        black_x.append(x)
        black_y.append(y)
        
    elif number1 == 'NA':
        x = 1
        y = number2
        black_x.append(x)
        black_y.append(y)
        
    elif number2 == 'NA':
        x = number1
        y = 0
        black_x.append(x)
        black_y.append(y)
    
    else: 
        x = float(number1)
        y = float(number2)
        x_convert = (2 ** abs(x))
        y_convert = -np.log10(y)
        
        if x < 0 and x_convert > 10 and y_convert > 30:
            label_x.append(x)
            label_y.append(y_convert)
            labels.append(label)
            
        elif x_convert > 10 and y_convert > 8:
            red_x.append(x)
            red_y.append(y_convert)
    
        else:
            black_x.append(x)
            black_y.append(y_convert)
    
    
panel1.scatter(red_x, red_y,
               s = 2,
               facecolor='red',
               linewidth = 0,
               alpha = 1)
        
panel1.scatter(black_x, black_y,
               s = 2,
               facecolor='black',
               linewidth = 0,
               alpha = 1)

panel1.scatter(label_x, label_y,
               s = 2,
               facecolor='red',
               linewidth = 0,
               alpha = 1)

for label in labels:
    i = labels.index(label)
    x = label_x[i]
    y = label_y[i]
    panel1.text(x,y,label+" ",fontsize=6, ha="right", va="center")


plt.savefig('Ahmed_Roshan_BME163_Assigmnment_Week3.png',dpi=600)

