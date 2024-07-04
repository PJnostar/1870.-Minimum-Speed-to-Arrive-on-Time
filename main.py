import trains
import trains_bin
import math
import random

dist = [1,3,2]
hours = 6

dist2 = [random.randint(1, 10) for i in range(10)]
hours2 = 14
print(dist2)

""" test1 = trains.Solution()
res1 = test1.minSpeedOnTime(dist, hours) 

print("min speed found: ", res1)
"""
test = trains_bin.Solution()
# print(test.minSpeedOnTime(dist2, hours2))

print(test.minSpeedOnTime(dist, hours))