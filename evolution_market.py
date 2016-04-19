#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from initial_market import StartMarket


class Agents(StartMarket):
    u"""Здесь реализованы базовые методы, которые
    применяются над популяцией агентов, а именно:
        — эволюция богатсва
        — обновление показателей у агентов в соответстии с эволюцией
        — переделавание показателей в массив, нужный в конечном счете для отрисовывания графика"""

    def wealth_evolution(self, realEstate, silver, price, delta_priceY, delta):
        z = self.rate - delta_priceY / (price + self.q / self.rate)
        k = np.divide(delta, max(0., z))
        wealth = silver + realEstate * price
        wantedEstate = ((wealth / (price + self.q / self.rate)) * min(k, 1) - realEstate)
        newEstate = realEstate + wantedEstate
        newSilver = (silver - wantedEstate * price - self.q * newEstate) * (1 + self.rate)
        return newEstate, newSilver

    def getWealthEvolutionAsRes(self, wealthOfAllDeltaArray, price, delta_priceX):
        newArrayOfAllDelta = []
        for wealthOfAgentsByOneDeltaArray in wealthOfAllDeltaArray:
            newArrayOfOneDelta = []
            for wealthOfOneAgentArray in wealthOfAgentsByOneDeltaArray:
                realEstate, silver, delta, nomer = wealthOfOneAgentArray[0], wealthOfOneAgentArray[1], wealthOfOneAgentArray[2], wealthOfOneAgentArray[3]
                estate, money = self.wealth_evolution(realEstate=realEstate, silver=silver,
                                                          price=price, delta_priceY=delta_priceX, delta=delta)
                newArrayOfOneDelta.append([estate, money, delta, nomer])
            newArrayOfAllDelta.append(newArrayOfOneDelta)
        return  newArrayOfAllDelta

    def getWealthArray(self, wealthOfAllDeltaArrayAsResX, price):
        wealthByDeltaArray = []
        for wealthOfAgentsByOneDeltaArray in wealthOfAllDeltaArrayAsResX:
            wealthByOneDelta = 0
            for wealthOfOneAgentArray in wealthOfAgentsByOneDeltaArray:
                realEstate, silver, deltaXXX = wealthOfOneAgentArray[0], wealthOfOneAgentArray[1], wealthOfOneAgentArray[2]
                wealthOfOneAgent = realEstate * price + silver
                wealthByOneDelta += wealthOfOneAgent
            wealthByDeltaArray.append(wealthByOneDelta)
        return wealthByDeltaArray

    def plotPurchases(self, wealth_array, price, delta_priceY):
        wantedEstateAll = []
        realEstateAll = []
        wealthAll = []
        for xarray in wealth_array:
            for yarray in xarray:
                realEstate, silver, delta, nomer = yarray[0], yarray[1], yarray[2], yarray[3]
                z = self.rate - delta_priceY / (price + self.q / self.rate)
                k = np.divide(delta, max(0., z))
                wealth = silver + realEstate * price
                wantedEstate = ((wealth / (price + self.q / self.rate)) * min(k, 1) - realEstate)
                wantedEstateAll.append(wantedEstate)
                realEstateAll.append(realEstate)
                wealthAll.append(wealth)
        plt.xlim([0, delta])
        #plt.plot(np.linspace(0, delta, len(wantedEstateAll)), wantedEstateAll, label="wanted")
        plt.plot(np.linspace(0, delta, len(realEstateAll)), realEstateAll, label="real")
        plt.plot(np.linspace(0, delta, len(wealthAll)), wealthAll, label="real")
        plt.plot([0, delta], [0, 0], color='red', label="zero level")
        plt.plot([z, z], [1, -1], color="m")
        plt.legend(loc="best")
        plt.draw()
        plt.clf()
