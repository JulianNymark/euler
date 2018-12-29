
sumOfSquares = sum([x**2 for x in range(1, 101)])
print('sumOfSquares: ', sumOfSquares)

squareOfSum = sum([x for x in range(1, 101)])**2
print('squareOfSum: ', squareOfSum)

diff = squareOfSum - sumOfSquares
print(diff)
