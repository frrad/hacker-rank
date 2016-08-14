import random
from  random import randint 

TOP = 25
NEG_PROB = .25

length = 0
size = randint(1,TOP)
print size
for x in xrange(size):
    if random.random()< NEG_PROB and length > 0:
        print '-'
        length -= 1
    else :
        print '+', random.randint(1,5)
        length += 1
