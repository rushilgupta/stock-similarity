import random
f = open('/Users/rgupta/Downloads/stock-similarity/stock.data', 'r+')
for i in xrange(10):
    for j in xrange(500000):
        f.write(str(i)+':'+str(random.randint(1, 1500000))+':1\n')