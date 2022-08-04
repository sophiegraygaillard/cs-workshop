# problem 02

current = 1
prev = 1
evenSum = 0

while current < 4000000:
  if current % 2 == 0:
    evenSum += current
  
  prevTmp = current
  current += prev
  prev = prevTmp

print(evenSum)