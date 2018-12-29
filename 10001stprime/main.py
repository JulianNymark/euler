import math


def genprimes(n):
    '''sieve of eratosthenes on array of length n'''
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


def convertPrimeBitmask2Primes(bitmasklist):
    thenewlist = []
    for i in range(len(bitmasklist)):
        if bitmasklist[i]:
            thenewlist.append(i + 1)
    thenewlist.pop(0)  # 1 is not a prime
    return thenewlist


def nthPrimeWithinSieve(inputNumber):
    '''this is very rough'''
    return int(10 ** (math.log(inputNumber, 10) + 1) * 2)


numberOfPrimesToSieve = nthPrimeWithinSieve(10001)
primes = convertPrimeBitmask2Primes(genprimes(numberOfPrimesToSieve))
print('the number is: ', primes[10000])

print(len(primes))
