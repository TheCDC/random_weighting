An algorithm that implements random selection of elements with arbitrary weighting.

Take as arguments a list of elements and an equal length list of weights.

For example:

from random_weighting import weighted_random
mythings = [1,2,3,4,5]
myweights = [1,2,1,3,1]
selection = weighted_random(mythings, myweights)
print(selection)