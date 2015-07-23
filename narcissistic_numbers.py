__author__ = 'AhmetOguzhan'

for i in range(2, 5):
    for j in xrange(10**(i-1), 10**i):
        if sum(int(x)**i for x in str(j)) == j:
            print j

raw_input("Done!")