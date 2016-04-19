#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from scipy.optimize import fsolve
from matplotlib import pyplot as plt
import numpy as np
import pickle
from initial_market import StartMarket
from evolution_market import Agents
from price_finder import PriceFinder
from create_market import init_agents
import matplotlib as mpl
from listOfSuccessfulAgents import listOfSuccesfulAgents  # фильтрация агентов
from filterUnluckyAgents import filterAgents # удаление невезучих агентов

if __name__ == '__main__':
    mpl.rcParams['legend.handlelength'] = 1
    #plt.ion()
    bigOlolo = []
    #wwwEvol = []
    #NBtemp = np.linspace(0.000193, 0.0248, 1)

    for temp in [0.]:
        q, newBuild, rate = 1., 0.00, 0.02
        xxx = init_agents(q=q, rate=rate, newBuild=newBuild)
        startMarket = StartMarket(q=q, rate=rate, newBuild=newBuild)
        agentsEvoltuion = Agents(q=q, rate=rate, newBuild=newBuild)
        priceFinder = PriceFinder(q=q, rate=rate, newBuild=newBuild)

        oldPrice = fsolve(xxx.createAgents, 5)
        print(u"первоначальная цена: " + str(oldPrice))
        print(u"невязка:             " + str(xxx.createAgents(oldPrice)))
        xxx.startAgents(oldPrice)
        waldRS = startMarket.getInitialPopulation()
        ololo = []

        print(u"Цена              Невязка\n" + str(temp))
        for i in range(1,2000):
            #newBuild *= (1 + temp)
            #agentsEvoltuion = Agents(q=q, rate=rate, newBuild=newBuild)
            #priceFinder = PriceFinder(q=q, rate=rate, newBuild=newBuild)
            if i == 100 :
                pickle.dump( waldRS, open( "asResG", "wb" ) )
                print(u"Конец")
                break
            priceX = priceFinder.solverPrice(oldPrice, waldRS)
            nevyazka = priceFinder.findPrice(priceX, oldPrice, waldRS)
            deltaPrice = priceX - oldPrice
            if (abs(nevyazka) > 0.001) or (priceX > 10e10):
                break
            print("{}   {}   {}".format(priceX, nevyazka, i))
            ololo.append(priceX)
            #www = agentsEvoltuion.getWealthArray(waldRS, priceX)
            #agentsEvoltuion.plotPurchases(wealth_array=waldRS, price=priceX, delta_priceY=deltaPrice)
            waldRS = agentsEvoltuion.getWealthEvolutionAsRes(waldRS, priceX, deltaPrice)
            assert isinstance(priceX, object)
            oldPrice = priceX
            #wwwEvol.append(www)
        plt.plot(np.linspace(0, len(ololo), len(ololo)), ololo)
        bigOlolo.append(ololo)
        
    plt.show()
    with open('priceZZZ', 'a') as f:
        pickle.dump(bigOlolo, f)


