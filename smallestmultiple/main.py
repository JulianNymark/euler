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


def convertBitMaskToListOfIndexesWhereTrue(bitmasklist):
    thenewlist = []
    for i in range(len(bitmasklist)):
        if bitmasklist[i]:
            thenewlist.append(i + 1)
    return thenewlist


def primeFactor(inputNumber):
    '''factorize the number into a sorted list its prime factors'''
    factors = []
    primes = convertBitMaskToListOfIndexesWhereTrue(genprimes(inputNumber))
    primes.pop(0)
    currentNumber = inputNumber
    while currentNumber > 1:
        for prime in primes:
            if currentNumber % prime == 0:
                factors.append(prime)
                currentNumber = currentNumber / prime
                break
    return factors


factorized = [primeFactor(x) for x in range(2, 21)]
[print(x) for x in factorized]

keeps = {}
for factors in factorized:
    '''
    special algorithm for counting the "longest chains"
    of ocurring factors
    '''
    temps = {}
    for factor in factors:
        key = str(factor)
        if key in temps:
            temps[key] += 1
        else:
            temps[key] = 1
    for key, val in temps.items():
        if key in keeps:
            if val > keeps[key]:
                keeps[key] = val
        else:
            keeps[key] = val

print(keeps)

prodSum = 1
for key, val in keeps.items():
    prodSum *= int(key) ** val
print('the number is: ', prodSum)
