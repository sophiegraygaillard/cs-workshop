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