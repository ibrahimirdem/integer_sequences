__author__ = 'aoozdemir'

for i in range(2, 10000):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print i

raw_input("Done!")