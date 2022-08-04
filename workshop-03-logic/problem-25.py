# problem 25

current = 1
prev = 1
i = 1

while len(str(current)) < 1000:
  prevTmp = current
  current += prev
  prev = prevTmp
  i += 1

print(i + 1)

