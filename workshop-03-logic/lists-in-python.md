# List: a data structure in Python
For today's practice questions, you will need one of Python data structures which is called a **list** (in R, it's called a vector). A `list` can store elements (ints, floats, objects, strings, etc.).

To instantiate (i.e create) a `list`, we use square brackets to denote a `list`.

```python
myList = []
```

`myList` is what we call an "empty list" which means it has no elements in it. But let's go ahead and create a new `list` that has something in it:

```python
anotherList = [3, 5, 1, 4, 2]
```

Our new variable, `anotherList`, now contains five `int` elements. Excellent! We now have a way of storing data when we code.

## How to access data in list?
But how do we access this data? We use something called "indexing" to access elements inside the list. In Python, we use a 0-index system which means that the first element in a list has a 0th index. The last element in the list has an index equal to the `length_of_the_list - 1`. To access a particular index (or indices), we use the index operator, `[]`, after a variable. Please observe the following code

```python
anotherList = [3, 5, 1, 4, 2]

anotherList[0] # this would return the number 3
anotherList[1] # this would return the number 5
anotherList[2] # this would return the number 1
anotherList[3] # this would return the number 4
anotherList[4] # this would return the number 2
```

This indexing system in Python is very flexible and we can actually do a lot more than just provide one index. Please observe the following code with index splicing (note the colon position): You'll see that the number after the colon is non-inclusive (i.e. the element at that index position is not included in the result).

A splice of `0:3` tells Python to get elements from the 0th index to the 3rd index, non-inclusive.

```python
anotherList = [3, 5, 1, 4, 2]

anotherList[0:3]  # this would return a list [3, 5, 1]
anotherList[1:3]  # this would return a list [5, 1]
anotherList[2:]   # this would return a list [1, 4, 2]
anotherList[:2]   # this would return a list [3, 5]
```

Another this we can do is get the length of the list.
```python
anotherList = [3, 5, 1, 4, 2]

len(anotherList) # this would return the value of 5
```

Lists are very powerful and there are a lot of different things that can be done. I encourage you to Google search your question if you come across a situation where you want to do an operator or manipulate a list. Here are two useful links that cover lists and indexing in more detail:
- [More about lists](https://www.tutorialspoint.com/python/python_lists.htm)
- [Indexing and splicing](https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf)


## Onto using a list
Great! We now have a data structure, but how do I add or remove elements to it? Or change elements? Let's see how we can do that.

We can add elements to the end of a list by using `.append()` which is a function visible to all objects with a `list` type.

```python
listOne = [3,5,2]
listOne.append(3)

print(listOne) # this would print [3,5,2,3]
```

We can also remove elements at the end of a list by using `.pop()`.
```python
listOne = [3,5,2]
listOne.pop() # the popping actually returns the final element, so would return 2 here

print(listOne) # this would print [3,5]
```

We can also remove elements at a specific index by using `del()`. Note that `del()` is a standalone function.
```python
listOne = [3,5,2]
del(listOne[1])

print(listOne) # this would print [3,2]
```

We can change elements at a specific index by using the index operator shown before.
```python
listOne = [3,5,2]
listOne[1] = 30000

print(listOne) # this would print [3,30000,2]
```

## Using loops to work with lists
We can conveniently use `for` loops to interact with our lists. Here is an example to sum up all the numbers in a list. This is a similar syntax to when we used `for i in range()` to build our `for` loops. We're replacing the `range()` with our list instead and having Python iterate over it, element by element.

```python
myList = [3,5,2,1]

total = 0
for element in myList:
    total += element

print(total) # this would return 11
```

This code above is equivalent to the following. Here we can go back to using our `range()` function in our `for` loop. Walk through this loop to convince yourself that this statement works.

```python
myList = [3,5,2,1]

total = 0
for i in range(0, len(myList), 1):
    total += myList[i] # remember that i is only 0, 1, 2, 3, etc... as set by the for loop. So we're using i to represent the index and we need to access the ith element in myList to save to our total.

print(total) # this would return 11
```

But wait, what if I want to only add every other element starting from the 0th element? 
```python
myList = [3,5,2,1]

total = 0
for i in range(0, len(myList), 2):
    total += myList[i]

print(total) # this would return 5 (a sum of 3 + 2)
```

Let's say that we want to save numbers that are divisible by 3 or 5 because we want to use those numbers later for future calculations.

```python
multiplesOfInterest = []
for i in range(1, 100, 1):
    if i % 3 == 0 or i % 5 == 0:
        multiplesOfInterest.append(i)

print(multiplesOfInterest)
# now we can do whatever we want with multiplesOfInterest which holds all the multiples of 3 or 5.
```

Now with this knowledge, go forth and try out those practice problems!