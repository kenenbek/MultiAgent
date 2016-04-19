#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from scipy.stats import chi2
import numpy as np
import random, pickle

def randomOfRandomness():
    """
    Здесь содержится функция, которая создаёт агентов с исходными данными
    """
    wealthOfAllDelta = []
    number = 0
    for i in np.linspace(0.00001, 0.061, 500):
        randomNumbers = []  #Список для хранения случайных чисел
        wealthDivided = []  # Богатство, поделенное случайным образом на случайное количество частей
        wealthOfOneDeltaASRS = []

        wealthOfOneDelta = 1000 * chi2.pdf(600 * i, 20)+0
        numberOfAgents = random.randint(1, 1)   # Какое количество агентов будет с одним дельта

        for ii in range(numberOfAgents):           # Добавление случайных чисел в список
            randomNumbers.append(random.randint(1,100))

        sumOfrandomAgents = sum(randomNumbers)

        for x in range(numberOfAgents): # Богатство поделено между агентами в рамках одного дельта
            wealthDivided.append(randomNumbers[x] * wealthOfOneDelta / sumOfrandomAgents)

        for wealth in wealthDivided:
            silver = random.uniform(0, wealth)
            realEstateMoney = wealth - silver
            number += 1
            wealthOfOneDeltaASRS.append([realEstateMoney, silver, i, number])

        wealthOfAllDelta.append(wealthOfOneDeltaASRS)

    #wealthOfAllDelta = np.array(wealthOfAllDelta)
    with open('simple_population', 'wb') as f:
        pickle.dump(wealthOfAllDelta, f)

    with open('numberOfagents', 'wb') as ff:
        pickle.dump(number, ff)
if __name__ == '__main__':
    randomOfRandomness()