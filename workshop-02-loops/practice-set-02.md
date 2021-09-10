# Practice question set #2

For questions 1-3, do not copy and paste to run the code. Work through the code by hand to answer the question.

## Question 1:
- What is the output of this chunk?

```python
for x in range(0, 15, 2):
  if x % 3 == 0:
    print(x)
```

## Question 2:
- What is the output of this chunk?

```python
counter = 0
total = 0

for x in range(0, 10, 1):
  counter += 1
  total = total + x

print(counter)
print(total)
```

## Question 3:
- What is the output of this chunk?

```python
x = 0
while x < 10:
  if x % 2 == 0:
      print(x)
  
  x += 1
```

## Question 4:
- What is the sum of all integers that are divisible by 8 from 1 to 1000 (inclusive)?

## Question 5:
- If your answer for Q4 was written using a `for` loop, write it using a `while` loop instead. If your answer for Q4 was written using a `while` loop, write it using a `for` loop instead.


# Answer key!
<details>
  <summary>Question 1 answer</summary>
  
  ```
  0
  6
  12
  ```
</details>



<details>
  <summary>Question 2 answer</summary>
  
  ```
  10
  45
  ```
</details>

<details>
  <summary>Question 3 answer</summary>

  ```
  0
  2
  4
  6
  8
  ```
</details>

<details>
  <summary>Question 4 answer</summary>
  
  Answer: 63000

  Code:
  ```python
  total = 0
  for i in range(1, 1001, 1):
    if i % 8 == 0:
      total += i
  
  print(total)
  ```
</details>

<details>
  <summary>Question 5 answer</summary>
  
  Answer: 63000

  Code:
  ```python
  total = 0
  counter = 1
  while counter <= 1000:
    if counter % 8 == 0:
      total += counter
    
    counter += 1
  
  print(total)
  ```
</details>