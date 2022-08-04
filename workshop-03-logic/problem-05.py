# problem 05

success = False
i = 20 * 19

while not success:
  success = True
  for j in range(11, 21):
    if i % j != 0:
      success = False
      break
  
  if not success:
    i += 20

print(i)