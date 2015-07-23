__author__ = 'aoozdemir'

for i in range(1, 20):
    a, b = 1, 1
    for j in range(i-1):
        a, b = b, a+b
    print a

raw_input("Done!")