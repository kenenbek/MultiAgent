#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pickle

class StartMarket:

    u"""Инициализация рынка с его показателями"""

    def __init__(self, rate, q, newBuild):
        self.rate = rate
        self.q = q
        self.newBuild = newBuild

    def getInitialPopulation(self):
        with open("a_population", 'rb') as f:
            wealthOfAllDeltaArrayAsResX = pickle.load(f)
        return wealthOfAllDeltaArrayAsResX