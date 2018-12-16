#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from scipy.stats import chi2
import numpy as np
import random, pickle
from scipy.optimize import fsolve
from initial_market import StartMarket
from matplotlib import pyplot as plt


class init_agents(StartMarket):

    def createAgents(self, price):
        wantedEstateAll = 0
        with open("simple_population", 'rb') as f:
            wealthOfAllDeltaArrayAsResX = pickle.load(f)

        for array in wealthOfAllDeltaArrayAsResX:
            for karray in array:
                wealth, realEstateMoney = karray[0] + karray[1], karray[0]
                z = self.rate - 0.025 * price / (price + self.q / self.rate)
                k = karray[2] * np.divide(1., max(0., z))
                wantedEstate = (wealth / (price + self.q / self.rate)) * min(k, 1) - realEstateMoney / price
                wantedEstateAll += wantedEstate
        wantedEstateAll -= self.newBuild
        return wantedEstateAll


    def startAgents(self, price):
        u"""Генерирует выборку с уже заданной ценой, посчитанной через fsovle
        и увеличивает количество денег на определенный процент
        И переделывает исходный массив в нумпи-массив"""

        with open("simple_population", 'rb') as f:
            wealthOfAllDeltaArrayAsResX = pickle.load(f)

        for arrayx in wealthOfAllDeltaArrayAsResX:
            for karray in arrayx:
                karray[0], karray[1] = (karray[0] / price[0]), karray[1] * (1 + self.rate)

        with open('a_population', 'wb') as f:
            pickle.dump(wealthOfAllDeltaArrayAsResX, f)
