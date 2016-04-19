#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib as mpl
from scipy.optimize import fsolve
from matplotlib import pyplot as plt
from initial_market import StartMarket
import numpy as np
import pickle

class PriceFinder(StartMarket):

    u"""Класс для того, чтобы находить цены, спрос, предложение и их разницу"""

    def findPrice(self, price, prev_price, wealthArrayRS):
        wantedEstateAll = 0.0

        for array in wealthArrayRS:
            for karray in array:
                realEstate, silver, delta = karray[0], karray[1], karray[2]
                wealth = realEstate * price + silver
                z = self.rate - (price - prev_price) / (price + self.q / self.rate)
                k = np.divide(delta, max(0., z))
                wantedEstate = ((wealth / (price + self.q / self.rate)) * min(k, 1.) - realEstate)
                wantedEstateAll += wantedEstate
        wantedEstateAll -= self.newBuild
        return wantedEstateAll

    def solverPrice(self, prev_price, wealthArrayRS):
        return fsolve(self.findPrice, prev_price, args=(prev_price, wealthArrayRS))

    def spros_i_predlojeine(self, price, prev_price, wealthArrayRS):
        spros, predlojenie, wantedEstateAll = 0, 0, 0

        for array in wealthArrayRS:
            for karray in array:
                realEstate, silver, delta = karray[0], karray[1], karray[2]
                wealth = realEstate * price + silver
                z = self.rate - (price - prev_price) / (prev_price + self.q / self.rate)
                k = delta * np.divide(1., max(0., z))
                wantedEstate = ((wealth / (price + self.q / self.rate)) * min(k, 1) - realEstate)
                wantedEstateAll += wantedEstate
                if wantedEstate >= 0:
                    spros += wantedEstate
                else:
                    predlojenie += wantedEstate
        wantedEstateAll -= self.newBuild
        return spros, predlojenie, wantedEstateAll

    def plotSPS(self, prev_price, wealthArrayRS):
        mpl.rcParams['legend.handlelength'] = 1
        xx = np.linspace(0, 100, 100)
        xx = xx.tolist()

        sprosArray, predlojArray, wantedEstateArray = [], [], []

        for ii in xx:
            sprosX, predlojX, wantedEstateX = self.spros_i_predlojeine(ii, prev_price, wealthArrayRS)
            sprosArray.append(sprosX)
            predlojArray.append(predlojX)
            wantedEstateArray.append(wantedEstateX)

        predlojArray = [(-1) * el for el in predlojArray]
        #f = open("l/decrease", "wb")
        #lo = [sprosArray, predlojArray, wantedEstateArray]
        #pickle.dump(lo, f)
        #f.close()

        plt.plot(xx, sprosArray, color='y', label="Demand")
        plt.plot(xx, predlojArray, color='r', label="Supply")
        plt.plot([prev_price, prev_price], [(-1) * max(sprosArray), max(sprosArray)], label='prev_price')
        plt.plot([xx[sprosArray.index(max(sprosArray))], xx[sprosArray.index(max(sprosArray))]], [(-1) * max(sprosArray), max(sprosArray)])
        #plt.scatter(xx[sprosArray.index(max(sprosArray))], max(sprosArray), marker='^',s=300, color='k', label='Maximum price')

        wantedEstateArray = [round(elem, 1) for elem in wantedEstateArray]
        #f = open('wantedArray.txt', 'w')
        #for element in wantedEstateArray:
            #f.write(str(element) + '\n')
        #f.close()
        #xx = [round(elem, 2) for elem in xx]

        #plt.scatter(prev_price, sprosArray[xx.index(round(prev_price, 2)-0.01)], marker='*', s=300, color="r", label='Previous price')
        #plt.scatter(xx[wantedEstateArray.index(0.0)], sprosArray[wantedEstateArray.index(0.0)], color="y",s=300, label='Current price')
        plt.xlabel("Price")
        plt.ylabel("Demand for housing unit")
        plt.legend(loc='upper left', numpoints=1)
        plt.grid()
        plt.show()

if __name__ == '__main__':
    pass