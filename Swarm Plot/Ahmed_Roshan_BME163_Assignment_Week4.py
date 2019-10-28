#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:49:50 2019

@author: roshanahmed
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import argparse
import random 

def argParser():
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--outputfile','-o',type=str, help='specify filename of your outputfile')
        parser.add_argument('--inputfile','-i',type=str, help='specify filename of your input')
        return vars(parser.parse_args())
    
args=argParser()
fileIn=args['inputfile']
fileName=args['outputfile']
      
figure_width = 7
figure_height = 3

plt.figure(figsize=(figure_width,figure_height))
panel_width = 5/figure_width
panel_height = 2/figure_height

panel1 = plt.axes([0.1,0.2,panel_width,panel_height])
panel1.set_xlim(.5,11.5)
panel1.set_ylim(75,100)

panel1.set_xticks([1,2,3,4,5,6,7,8,9,10,11])
panel1.set_xticklabels(['1','2','3','4','5','6','7','8','9','10','>10'])

panel1.set_xlabel('Subread coverage')
panel1.set_ylabel('Identity (%)')

#panel2 = plt.axes([0.9, 0.2, 0.2/figure_width, panel_height])
#panel2.set_xticks([])
#panel2.set_ylim(7,15)
#panel2.set_yticks([7,8,9,10,11,12,13,14,15])
#panel2.set_yticklabels(['7','8','9','10','11','12','13','14','15'])
#panel2.set_ylabel('Read quality (Q)')


medians = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
bins = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11]

#qualityScoresDict = {}
keys = {1,2,3,4,5,6,7,8,9,10,11}
qualityScoresDict = dict.fromkeys(keys) 
colorDict = {}


for line in open("BME163_Input_Data_3.txt"):
    a =line.strip().split('\t')
    longString = (a[0])
    values = longString.split("_")
    percent = float(a[1])
    q_score = float(values[1])
    subread = int(values[3])

    if subread == 1:
        list1.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 2:
        list2.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 3:
        list3.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 4:
        list4.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 5:
        list5.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 6:
        list6.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 7:
        list7.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 8:
        list8.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 9:
        list9.append(percent)
        qualityScoresDict[subread] = (q_score)
    elif subread == 10:
        list10.append(percent)
        qualityScoresDict[subread] = (q_score)
    else:
        list11.append(percent)
        qualityScoresDict[11] = (q_score)
    
        



"""
Randomly Subsample Lists
"""

dictionary = {j:[] for j in range (1,12)}
for lists in bins:
    random_point = random.sample(lists, 1000)
    a = bins.index(lists)
    dictionary[a + 1] = random_point
#    print(dictionary)

"""
math
"""    

#print(dictionary.keys())
for i in dictionary.keys():
    points = []
    panel1.plot(i, dictionary.get(i)[0],
                color = 'black',
                markersize = 1,
                markerfacecolor = 'black',
                linewidth = 0,
                alpha = 1)
    points.append([i, dictionary.get(i)[0]])
#    print(dictionary.get(i)[0])
#    print(points)
    for y_val in sorted(dictionary.get(i)):
        x = i 
        flag = 0 
        while flag == 0:
            distance = []
            for pt in points:
                a = ((((x - pt[0])/11)*5)**2)
                b = ((((y_val - pt[1])/25)*2)**2)
                c = np.sqrt(a+b)
#                print(c)
                distance.append(c)
#                print(distance)
#                flag = 1
            if min(distance)>0.009:
                panel1.plot(x,y_val,
                            color='black',
                            marker= "o",
                            markeredgecolor='black',
                            markeredgewidth=0,
                            markerfacecolor='black',
                            markersize= .75,
                            linewidth=0,
                            linestyle='--',
                            alpha=1)
                points.append([x,y_val])
                flag = 1
            elif dictionary.get(i).index(y_val) % 2 == 0:
                x = (x + .002)
            else:
                x = (x - .002)
                
                
for lists in bins:
    medians.append(np.median(lists))

for i in range(0,11):
    plt.hlines(medians[i], .585 + i, 1.415 + i, 
               colors='red', 
               linestyles='solid', 
               linewidth = .8)
    
dashes = [4,8,8,8]
line, = plt.plot([0,12],[95,95,], 
                '--',
                linewidth = 0.6,
                color = '0.25',
                label = "set_dashes({0})".format(dashes))
line.set_dashes(dashes)

        
plt.savefig('Week4_Fixed',dpi=600)







        

    


