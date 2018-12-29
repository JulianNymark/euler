import math
import time


# sieve of eratosthenes on array of length n
def genprimes(n):
    primes = [True] * n
    increasingCoefficient = 2  # first 2's, then 3's ... (but multiples)
    upTo = math.ceil((math.sqrt(n)) + 1)

    while (increasingCoefficient <= upTo):
        i = 2
        checkNumber = i * increasingCoefficient
        while (checkNumber <= n):
            primes[checkNumber - 1] = False
            i += 1
            checkNumber = i * increasingCoefficient
        increasingCoefficient += 1

    return primes


def convertBitMaskToListOfIndexesWhereTrue(bitmasklist):
    thenewlist = []
    for i in range(len(bitmasklist)):
        if bitmasklist[i]:
            thenewlist.append(i + 1)
    return thenewlist


def getLargestPrimeFactor(magicNumber):
    upTo = math.ceil((math.sqrt(magicNumber)) + 1)
    theprimes = convertBitMaskToListOfIndexesWhereTrue(
        genprimes(upTo))
    for prime in reversed(theprimes):
        if (magicNumber % prime == 0):
            return prime


# print('find 10 primes')
# genprimes(10)
# print('find 1000 primes')
# genprimes(1000)
# print('find 10000 primes')
# genprimes(10000)
# print('find 100000 primes')
# genprimes(100000)

print('the number is: ', getLargestPrimeFactor(600851475143))
