#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np

def filterAgents(listOfAgents, wealthRS):
    u"""Метод фильтрации агентов, которым не повезло.
    Данный метод будет использоваться для, того чтобы
    удалять агентов; для нахождения цены неджимости в данный момент времени
    listOfAgents — список везучих агентов
    wealthRS — исходный массив для сортировки
    """
    wealthRSCopy = np.copy(wealthRS)
    for array in wealthRSCopy:
        for i, karray in enumerate(array):
            if karray[3] not in listOfAgents:
                array[i] = np.array([0., 0., 0., 0.])

    wealthRSZero = wealthRS - wealthRSCopy
    return wealthRSCopy, wealthRSZero


