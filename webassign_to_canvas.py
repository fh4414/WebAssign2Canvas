# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:53:59 2021

@author: cvkelly
Christopher V Kelly
Associate Professor
Department of Physics and Astronomy
Wayne State University
cvkelly@wayne.edu
https://cvkelly.wayne.edu

"""

import numpy as np
import matplotlib.pyplot as plt


fold = r'C:\Users\cvkelly\OneDrive - Wayne State University\T - teaching\PHY 2130 - Physics fo the Life Sciences I - F21\Convert webassign to canvas/'
wfile = 'webassign.csv'
cfile = 'canvas.csv'


# %%
if 1: # read stuff
    file = open(fold+wfile, 'r')
    Lines = file.readlines()
    # was = np.loadtxt(fold+cfile,delimiter='1',skiprows=1)

    for i in range(10):
        if Lines[i][:8] == 'Fullname':
            onebefore = i
            break

    maxscores = Lines[onebefore-2]
    maxscores = maxscores.replace('Totals','MaxScores',)
    for iii in range(4):
        maxscores = maxscores.replace(',,',',')
    maxscores = 'MaxScores,MaxScores,MaxScores,'+maxscores
    # print(maxscores)

    rowlab = Lines[onebefore-4]
    rowlab = rowlab.replace('"','')
    rowlab = rowlab.replace(',,',',Assignment Name,')
    # print(rowlab)


    Lines = Lines[(onebefore+1):]

    firstnames = []
    lastnames = []
    scores = []
    cnt = -1
    for lin in Lines:
        if len(lin) == 0:
            break
        cnt += 1
        # print(lin)
        f = lin.find('",')
        fullname = lin[1:f].upper()
        f = fullname.find(', ')
        firstnames.append(fullname[(f+2):])
        lastnames.append(fullname[:f].upper())

        f = lin.find('%,')
        score = lin[(f+2):-1]
        score = score.replace('*','6')
        score = score.replace('ND','0')
        score = score.replace('NS','0')
        score = score.split(',')
        for j in range(len(score)):
            score[j] = float(score[j])
        scores.append(score)

    scores = np.array(scores)

    file.close()

# %%
if 1:
    # # %% read the Canvas names
    file = open(fold+cfile,'r')
    Lines = file.readlines()
    Lines = Lines[:]
    clastnames = []
    cfirstnames = []
    scnt = -1
    for lin in Lines:
        scnt += 1
        f = lin.find('",')
        fullname = lin[1:f].upper()
        f = lin.find(',')
        clastnames.append(fullname[:(f-1)].upper())
        cfirstnames.append(fullname[(f+1):].upper())
    file.close()

# %% remove funny symbols
symstoremove = [' ','-','5','6','7','8','9','1','0','2','3','4','_','+','#']
varstocheck = [lastnames,firstnames,clastnames,cfirstnames]

for i,varnow in enumerate(varstocheck):
    for j,sym in enumerate(symstoremove):
        for k in range(len(varnow)):
            varnow[k] = varnow[k].replace(sym,'')
    varstocheck[i] = varnow

lastnames = varstocheck[0]
firstnames = varstocheck[1]
clastnames = varstocheck[2]
cfirstnames = varstocheck[3]

# %% matchnames
towhichcanvas = np.zeros(scores.shape[0])
towhichcanvasnum = np.zeros(scores.shape[0])
for s in range(scores.shape[0]):
    found = 0
    for j in range(len(clastnames)):
        if (firstnames[s] == cfirstnames[j] and lastnames[s] == clastnames[j]):
            towhichcanvas[s]=j
            found += 1
    towhichcanvasnum[s] = found

for s in range(scores.shape[0]):
    if towhichcanvasnum[s]>1:
        print('Error with ',firstnames[s],lastnames[s])

print('Round 1: success for ',np.sum(towhichcanvasnum==1),' of ',len(towhichcanvasnum))

# %%
for s in range(scores.shape[0]):
    found = 0
    if towhichcanvasnum[s] == 0:
        for j in range(len(clastnames)):
            if lastnames[s] == clastnames[j]:
                # print(lastnames[s], clastnames[j])
                found += 1
                towhichcanvas[s] = j
        towhichcanvasnum[s] = found

for s in range(scores.shape[0]):
    if towhichcanvasnum[s]>1:
        print('Error with ',firstnames[s],lastnames[s])

print('Round 2: success for ',np.sum(towhichcanvasnum==1),' of ',len(towhichcanvasnum))

# %%
towhichcanvas = towhichcanvas.astype(np.int32)

# for s in range(scores.shape[0]):
#     if towhichcanvasnum[s] != 1:
#         if scores[s,0] > np.percentile(scores[:,0],10):
#             print('Not found in Canvas: ',
#                   lastnames[s],
#                   firstnames[s],scores[s])
# %% verify
# if 1:
#     for s in range(scores.shape[0]):
#         print(firstnames[s],
#               cfirstnames[towhichcanvas[s]],
#               lastnames[s],
#               clastnames[towhichcanvas[s]])


# %% print results
f = open('webassign_out.csv','w')
f.write(rowlab)
f.write(maxscores)

sc = np.argsort(towhichcanvas)
# sc = sc[::-1]
zeros = '0'
for i in range(scores.shape[1]-1):
    zeros = zeros+',0'
zeros = zeros+'\n'

cnt = 0
for s in sc :
    if towhichcanvas[s] == 0:
        continue
    if towhichcanvas[s] > cnt:
        while towhichcanvas[s] > cnt:
            f.write('NA,NA,NA,NA,'+zeros)
            cnt += 1
            # if towhichcanvas[s] < cnt:
        while towhichcanvas[s] < cnt:
            # f.write('0,0,0,0,0\n')
            cnt -= 1
    sn = str(scores[s])
    sn = sn.replace('[','')
    sn = sn.replace(']','')
    sn = sn.replace('\n','')
    sn = sn.replace(' ',',')
    for iii in range(4):
        sn = sn.replace(',,',',')
    if sn[-1]==',':
        sn = sn[:-1]

    f.write(lastnames[s]+','+clastnames[towhichcanvas[s]]+','+firstnames[s]+','+cfirstnames[towhichcanvas[s]]+','+sn+'\n')
    cnt += 1

f.close()