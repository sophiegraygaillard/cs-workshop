# problem 06 - vinny

sumOfSquares = 0
squareOfSums = 0
for i in range(1, 101, 1):
  sumOfSquares += i ** 2
  squareOfSums += i

squareOfSums = squareOfSums ** 2

print(squareOfSums - sumOfSquares)