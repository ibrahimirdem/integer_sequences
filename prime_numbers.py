__author__ = 'aoozdemir'

print 2

for i in range(3, 500):
    divided = False
    for j in range(2, i):
        if i % j == 0:
            divided = True

    if divided == False:
        print i

raw_input("Done!")
