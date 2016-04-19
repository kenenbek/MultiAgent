#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
from matplotlib import pylab
import pickle
import numpy as np
from scipy.stats import chi2

evolution = pickle.load(open("evolution", 'r'))
data = [evolution[0], evolution[120], evolution[300], evolution[400], evolution[466], evolution[499], evolution[506]]

#with open('little_evolution', 'wb') as f:
    #pickle.dump(data, f)

raps = np.linspace(0.00001, 0.061, 500)
linestyles = ['-', '--', '-.', '-', '-', '--', '-']
for i, el in enumerate(linestyles):
    if (i == 6) or (i == 0):
        lw = 2.5
    else: lw = 1
    plt.plot(raps, data[i], el, lw=lw, label=str(i) + ' period')
plt.xlim([0, 0.061])
plt.legend(loc="best")
plt.xlabel("Time preference parameter", fontsize=15)
plt.ylabel("Wealth of agents", fontsize=15)
plt.ylim([0, 216])
plt.show()









"""
import matplotlib.pyplot as plt
import pickle
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import matplotlib as mpl

import numpy as np
xx = np.linspace(0, 100, 1000)
xx = xx.tolist()
xx = [round(elem, 2) for elem in xx]
mpl.rcParams['legend.scatterpoints'] = 1
prev_price, prev_price2 = 53.66, 60.071  #62.456

increase_demand = pickle.load(open("l/increase", "rb"))
decrease_demand = pickle.load(open("l/decrease", "rb"))
sprosArray, predlojArray, wantedEstateArray = increase_demand[0], increase_demand[1], increase_demand[2]
sprosArray2, predlojArray2, wantedEstateArray2 = decrease_demand[0], decrease_demand[1], decrease_demand[2]

wantedEstateArray = [round(elem, 1) for elem in wantedEstateArray]
wantedEstateArray2 = [round(kot, 1) for kot in wantedEstateArray2]
predlojArray = [(-1) * el for el in predlojArray]
predlojArray2 = [(-1) * kk for kk in predlojArray2]

###
fig, ax = plt.subplots(figsize=[5, 4])
plt.title("A growing market", fontsize=20)
plt.grid()
plt.xlim([0, 100])
#plt.ylim()
plt.plot(xx, sprosArray, color='b', lw=3.5, label="Demand")
plt.plot(xx, predlojArray, color=(255/255, 79/255, 0/255), lw=3.5, label="Supply")
plt.xlabel("Price", fontsize=20)
plt.ylabel("Demand for real estate", fontsize=20)
#plt.scatter(prev_price, sprosArray[xx.index(round(prev_price, 2)-0.01)], marker='*', color="r", label='Previous price', s=150)
#plt.scatter(xx[wantedEstateArray.index(0.0)], sprosArray[wantedEstateArray.index(0.0)], color="y", label='Current price', s=150)
#plt.scatter(xx[sprosArray.index(max(sprosArray))], max(sprosArray), marker='^', color='k', label='Max price', s=150)
plt.legend(loc=3, fontsize=16)

x1, x2, y1, y2 = 52.95, 56.9, 44.2, 45.56
axins = inset_axes(ax, loc=1, width="53%", height=2.5) # zoom = 2
axins.plot(xx, sprosArray, color='b', lw=2, label="Demand")
axins.plot(xx, predlojArray, color=(255/255, 79/255, 0/255), lw=2, label="Supply")
a23 = axins.scatter(prev_price, sprosArray[xx.index(round(prev_price, 2)-0.01)], marker='*', color="r", label='Previous price', s=150, zorder=3)
a22 = axins.scatter(xx[wantedEstateArray.index(0.0)], sprosArray[wantedEstateArray.index(0.0)], color="y", label='Current price', s=150, zorder=3)
a11 = axins.scatter(xx[sprosArray.index(max(sprosArray))], max(sprosArray), marker='^', color='k', label='Max price', s=150, zorder=3)
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
#plt.xticks(visible=False)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=4, loc2=3, fc="none", ec="0.", zorder=3)
plt.figlegend((a11, a22, a23), ('Maximum price','Current price', 'Previous price'), 1)
plt.draw()



fig, ax = plt.subplots()
plt.grid()
plt.title("A failing market", fontsize=20)
plt.xlim([0, 100])
plt.ylim([0, 175])
plt.plot(xx, sprosArray2, color='b', lw=3.5, label="Demand")
plt.plot(xx, predlojArray2, color=(255/255, 79/255, 0/255), lw=3.5, label="Supply")
a23 = plt.scatter(xx[sprosArray2.index(max(sprosArray2))], max(sprosArray2), marker='^',s=150, color='k', zorder=3)
a11 = plt.scatter(prev_price2, sprosArray2[xx.index(round(prev_price2, 2)-0.01)], marker='*', s=150, color="r", zorder=3)

plt.xlabel("Price", fontsize=20)
plt.ylabel("Real estate's supply", fontsize=20)
plt.legend(loc=3, fontsize=16)

x1, x2, y1, y2 = 54, 66, -3, 145
#axins = inset_axes(ax) #, loc=3, width="45%", height=2.5) # zoom = 2
axins = inset_axes(ax, width=4, height=3,  loc=3,
                 bbox_to_anchor=(0.15, 0.25),
                 bbox_transform=ax.figure.transFigure)
plt.plot(xx, sprosArray2, color='b', lw=1, label="Demand")
plt.plot(xx, predlojArray2, color=(255/255, 79/255, 0/255), lw=1, label="Supply")
a22 = plt.scatter(xx[wantedEstateArray2.index(-0.1)], sprosArray2[wantedEstateArray2.index(-0.1)]+0.08, color="y",s=150, label='Current price', zorder=3)
plt.figlegend((a23, a22, a11), ('Maximum price','Current price', 'Previous price'), 1)
plt.xlim([57, 58.5])
plt.ylim([-0, 0.5])
plt.draw()
plt.tick_params(axis='both', which='major', labelsize=10)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.", zorder=3)
plt.show()"""




