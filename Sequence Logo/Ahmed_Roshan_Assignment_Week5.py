#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:03:48 2019

@author: roshanahmed
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import argparse
import sys


def argParser():
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--outputfile','-o',type=str, help='specify filename of your outputfile')
        parser.add_argument('--inputfile','-i',type=str, help='specify filename of your input')
        return vars(parser.parse_args())
    
args=argParser()
fileIn=args['inputfile']
fileName=args['outputfile']
plt.style.use('BME163.mplstyle')
      

figure_width = 6
figure_height = 3

panel_width = 2.4/figure_width
panel_height = 1/figure_height

plt.figure(figsize=(figure_width, figure_height))

panel1 = plt.axes([0.083,0.3,panel_width,panel_height])
panel1.set_xlim(-10,10)
panel1.set_ylim(0,2)
panel1.set_xticks([-10,-5,0,5,10])
panel1.set_xticklabels(["-10","-5","0","5","10"])
panel1.set_xlabel('Distance to\nSplice Site')
panel1.set_ylabel('Bits')
panel1.set_title('5\'SS')
panel1.axvline(x=0,color='black',linewidth=0.5)

panel2 = plt.axes([0.5665,0.3,panel_width,panel_height])
panel2.set_xlim(-10,10)
panel2.set_ylim(0,2)
panel2.set_xticks([-10,-5,0,5,10])
panel2.set_xticklabels(["-10","-5","0","5","10"])
panel2.set_yticks([])
panel2.set_xlabel('Distance to\nSplice Site')
panel2.set_title('3\'SS')
panel2.axvline(x=0,color='black',linewidth=0.5)

A = mpimg.imread('A.png')
C = mpimg.imread('C.png')
G = mpimg.imread('G.png')
T = mpimg.imread('T.png')

headerList = []
sequenceList = []
threeSplice = []
fiveSplice = []
relA = []
relC = []
relG = []
relT = []
relNuc = [relA, relC, relG, relT]
heightA = []
heightC = []
heightG = []
heightT = []
indexList = []

for line in open("Splice_Sequences.fasta"):
    if line.startswith(">"):
        header = line[1:].rstrip()
        headerList.append(header)
    else:
        seq = line.rstrip()
        sequenceList.append(seq)

for index in headerList:
    if index.startswith("5"):
        x = headerList.index(index)
        y = sequenceList[x].upper()
        fiveSplice.append(y)
    elif index.startswith("3"):
        x = headerList.index(index)
        y = sequenceList[x].upper()
        threeSplice.append(y)

for index in range(0,20):
    indexList.clear()
    for seq in threeSplice:
        indexList.append(seq[index])

    n = len(indexList)
    relA.append(indexList.count('A')/n)
    relC.append(indexList.count('C')/n)
    relG.append(indexList.count('G')/n)
    relT.append(indexList.count('T')/n)
    

for i in range(0,20):
    freqDict = {"A":0,"C":0,"G":0,"T":0}
    for nuc in relNuc:
        if nuc[i] is relA[i]:
            value = {"A": nuc[i]}
            freqDict.update(value)
        elif nuc[i] is relC[i]:
            value = {"C": nuc[i]}
            freqDict.update(value)
        elif nuc[i] is relG[i]:
            value = {"G": nuc[i]}
            freqDict.update(value)
        elif nuc[i] is relT[i]:
            value = {"T": nuc[i]}
            freqDict.update(value)
            
    shanEntropy = -1 * np.sum(freqDict[x] * np.log2(freqDict[x]) for x in freqDict)
    sampleCorrect = 3/((np.log(2)) * (2 * n))
    heights = {x:freqDict[x] * (2 - (shanEntropy + sampleCorrect)) for x in freqDict}
    sortedHeights = dict(sorted(heights.items(),key=lambda kv:kv[1]))
    y_height = 0
    
    for nuc in sortedHeights.keys():
        if nuc is "A":
            panel2.imshow(A, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
            y_height = y_height + sortedHeights.get(nuc)
        elif nuc is "C":
             panel2.imshow(C, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
             y_height = y_height + sortedHeights.get(nuc)
        elif nuc is "G":
             panel2.imshow(G, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
             y_height = y_height + sortedHeights.get(nuc)
        elif nuc is "T": 
             panel2.imshow(T, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
             y_height = y_height + sortedHeights.get(nuc)
    

relA = []
relC = []
relG = []
relT = []
relNuc = [relA, relC, relG, relT]
heightA = []
heightC = []
heightG = []
heightT = []
indexList = []

for index in range(0,20):
    indexList.clear()
    for seq in fiveSplice:
        indexList.append(seq[index])
    
    n = len(indexList)
    relA.append(indexList.count('A')/n)
    relC.append(indexList.count('C')/n)
    relG.append(indexList.count('G')/n)
    relT.append(indexList.count('T')/n)
    
for i in range(0,20):
    freqDict = {"A":0,"C":0,"G":0,"T":0}
    for nuc in relNuc:
        if nuc[i] is relA[i]:
            value = {"A": nuc[i]}
            freqDict.update(value)
        elif nuc[i] is relC[i]:
            value = {"C": nuc[i]}
            freqDict.update(value)
        elif nuc[i] is relG[i]:
            value = {"G": nuc[i]}
            freqDict.update(value)
        elif nuc[i] is relT[i]:
            value = {"T": nuc[i]}
            freqDict.update(value)
            
    shanEntropy = -1 * np.sum(freqDict[x] * np.log2(freqDict[x]) for x in freqDict)
    sampleCorrect = 3/((np.log(2)) * (2 * n))
    heights = {x:freqDict[x] * (2 - (shanEntropy + sampleCorrect)) for x in freqDict}
    sortedHeights = dict(sorted(heights.items(),key=lambda kv:kv[1]))
    y_height = 0
    
    for nuc in sortedHeights.keys():
        if nuc is "A":
            panel1.imshow(A, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
            y_height = y_height + sortedHeights.get(nuc)
        elif nuc is "C":
             panel1.imshow(C, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
             y_height = y_height + sortedHeights.get(nuc)
        elif nuc is "G":
             panel1.imshow(G, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
             y_height = y_height + sortedHeights.get(nuc)
        elif nuc is "T":
             panel1.imshow(T, extent = [(i-10),(i-9), y_height, y_height + (sortedHeights.get(nuc))],
                                    origin='upper', aspect='auto')
             y_height = y_height + sortedHeights.get(nuc)
    

plt.savefig('Ahmed_Roshan_Assignment_Week5',dpi=600)