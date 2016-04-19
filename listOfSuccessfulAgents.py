#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random, pickle

def listOfSuccesfulAgents(n):
    with open("numberOfagents", 'rb') as f:
        numberOfAgents = pickle.load(f)
    arrayX = set()
    x =  0
    while x < numberOfAgents:
        b = x
        x = int(random.expovariate(n))
        x += b
        arrayX.add(x)
    listArray = list(arrayX)
    listArray.sort()
    listArray = listArray[:-1]
    listArray.append(numberOfAgents)
    return listArray