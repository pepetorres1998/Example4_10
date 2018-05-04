import random
import sys

print(random.randint(1, 32769))

a = sys.argv[1]

def generateBinary(a):
    list = []
    for i in range(int(a)):
        list.append("{0:015b}".format(random.randint(1, 32769)))
    return list

blist = generateBinary(a)
print(blist)
print(True == 1)
