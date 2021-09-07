# Practice question set #1

## Question 1:
- What is the output of this chunk?

```python
numCells = 3000
numPlates = 3
maxCellsPerWell = 2000

if numCells / numPlates <= maxCellsPerWell:
  print("proceed with loading")

elif numCells / numPlates > maxCellsPerWell:
  print("do not proceed with loading")
```

## Question 2:
- What is the output of this chunk?
- What is the difference between this code chunk and the one above?

```python
numCells = 3000
numPlates = 3
maxCellsPerWell = 2000

if numCells / numPlates <= maxCellsPerWell:
  print("proceed with loading")

else:
  print("do not proceed with loading")
```

## Question 3:
- What is the output of this chunk if `usedAbs` is set to `1`? `5`? `9`? `10`? `12`?

```python
# change the below variable to 1, 5, 9, 10, 12 when you answer this question
usedAbs = 0

if usedAbs < 3:
  print("small panel")
elif usedAbs > 10:
  print("some large panel")
elif usedAbs < 8 and usedAbs <= 10:
  print("a very different type of panel")
elif usedAbs == 10:
  print("a nice 10 color panel")
elif usedAbs == 9:
  print("a nice 9 color panel")
else:
  print("an unknown panel")
```

## Question 4:
- Step 1: Create a variable named x and set it to a non-zero integer.
- Step 2: Print out messages saying if x is a multiple of 3, multiple of 5, both, or neither.
- Note: Your code should be as concise as possible for this question. For example, 15 should print "both" and not "multiple of 3", "multiple of 5", and "both" (edited) 

# Answer key!
<details>
  <summary>Question 1 answer</summary>
  
  ```
  proceed with loading
  ```
</details>



<details>
  <summary>Question 2 answer</summary>
  
  ```
  proceed with loading
  ```
  The code is essentially the same, although the code shown in Question 2 is the preferred format because the `elif numCells / numPlates > maxCellsPerWell:` seen in Question 1 is implied with the `else` used in Question 2.
</details>

<details>
  <summary>Question 3 answer</summary>

  ```
  1
  small panel

  5
  a very different type of panel

  9
  a nice 9 color panel

  10
  a nice 10 color panel

  12
  some large panel
  ```
</details>

<details>
  <summary>Question 4 answer</summary>
  
  ```python
  x = 7

  if x % 3 == 0 and x % 5 == 0:
    print("both")
  elif x % 3 == 0:
    print("divisible by 3")
  elif x % 5 == 0:
    print("divisible by 5")
  else:
    print("neither")
  ```
</details>

