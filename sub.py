import numpy as np
from numba import njit


@njit
def checkBuyCard(gems, perGems, price):
    temp_ = gems[0:5] + perGems
    if np.sum((price > temp_)*(price - temp_)) <= gems[5]:
        return True
    
    return False


@njit
def openCard(env, lv1, lv2, lv3, cardId, posE):
    if cardId < 40:
        if lv1[-1] < 40:
            env[posE] = lv1[lv1[-1]]
            lv1[-1] += 1
        else:
            env[posE] = -1
    elif cardId < 70:
        if lv2[-1] < 30:
            env[posE] = lv2[lv2[-1]]
            lv2[-1] += 1
        else:
            env[posE] = -1
    else:
        if lv3[-1] < 20:
            env[posE] = lv3[lv3[-1]]
            lv3[-1] += 1
        else:
            env[posE] = -1