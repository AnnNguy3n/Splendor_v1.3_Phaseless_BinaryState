from env import *
from time import time as time_ns

perFile = List()
perFile.append(np.array([[0.]]))

t_ = time_ns()
a, b = main([randomBot, randomBot, randomBot, randomBot], 100, perFile, True, 100)
print(a, time_ns()-t_)

t_ = time_ns()
a, b = main([randomBot, randomBot, randomBot, randomBot], 100, perFile, True, 100)
print(a, time_ns()-t_)

t_ = time_ns()
a, b = main([randomBot, randomBot, randomBot, randomBot], 1000, perFile, True, 100)
print(a, time_ns()-t_)

t_ = time_ns()
a, b = main([randomBot, randomBot, randomBot, randomBot], 10000, perFile, True, 1000)
print(a, time_ns()-t_)

t_ = time_ns()
a, b = main([randomBot, randomBot, randomBot, randomBot], 100000, perFile, True, 1000)
print(a, time_ns()-t_)