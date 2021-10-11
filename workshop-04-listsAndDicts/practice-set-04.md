# Practice question set #4

For this week's practice set, we'll be preparing some code that we'll use to learn about functions in next week's workshop. For next week, we'll be compartmentalizing our code to have more efficient and reproducible code.

For next week, we'll be making an program that will analyze some data. This problem set will set the scene for this program.

---
### **DO NOT SKIP THIS PORTION.** Before you start the practice problems, make sure you have read the other two files (lists-in-python.md and dicts-in-python.md) in this folder before proceeding with these questions!
---

## Practice question 1 - list practice
  1. Create a list called `myFavoriteNumbers` and set it to your 5 favorite numbers with the first element being your most favorite and last element being your least favorite.
  2. Add any number to the end of your list.
  3. Print out the third element.
  4. Print out the 1st, 2nd, and 3rd element, using one line of code.
  5. Print out your list in reverse order, using one line of code.
  6. Find the sum of your list using a `for` loop.

  <details>
  <summary>Question 1 answer</summary>
  
  ```python
  # creating a list of my favorite numbers
  myFavoriteNumbers = [1, 10, 100, 1000, 10000]

  # add a number to end of list
  myFavoriteNumbers.append(300)

  # print out third element. remember that python is a 0-index based language!
  print(myFavoriteNumbers[2])

  # print out 1st, 2nd, and 3rd elements with one line
  print(myFavoriteNumbers[0:3])

  # print out list in reverse order, using one line of code
  print(myFavoriteNumbers[::-1])

  # find sum using a for loop
  numSum = 0
  for x in myFavoriteNumbers:
    numSum += x
  ```
</details>

## Practice question 2 - dict practice
  1. Create a dictionary called `myFavoritePipettes`. You need two keys `20ulPipette` and `1000ulPipette`. For each key, set a value consisting of the reason why you like that pipette.
  2. In this dictionary, set a new key called `200ulPipette` and give it a value of `"much versatile, such wow"`.

<details>
  <summary>Question 2 answer</summary>
  
  ```python
  myFavoritePipettes = {"20ulPipette": "versatile",
  "1000ulPipette": "robust"}

  myFavoritePipettes["200ulPipette"] = "much versatile, such wow"
  ```
</details>

## Practice question 3 - preparing for next week
We will be importing some dummy flow data for practice. The values don't really matter for this code as I just chose random numbers.

I have imported the below table into a nested list for you. Use this list called `flowData` for your code. This list consists of 4 sub-lists, one for each row of the dummy tsv file. The first sub-list is the header, and the other lists contain the data. The first element of each sub-list refers to the sampleID, second elmenet refers to CD3 percentage, etc.

| sampleID | CD3 | CD4 | CD8 |
|:---:|:--:|:---:|:---:|
stim | 58.3 | 24.3 | 20.5
noStim | 32.1 | 34.2 | 50.3
PMAstim | 34.3 | 15.3 | 31.3

For this question, convert this list into a dictionary, where...
 1. Each key in the dictionary are the column names found in the header (i.e. the first sub-list).
 2. Each value is a list containing the column's data.

For instance, if my new dictionary is called `flowDataDict`, I should be able to run
`flowDataDict["sampleID"]` to get a list containing `["stim", "noStim", "PMAstim"]`. Similarly, `flowDataDict["CD3"]` should return a list of values `[58.3, 32.1, 34.3]`.

Notes:
- You should not be manually entering the data into the dictionary. Use what we have learned with `for` loops and what you know about list indexing from the tutorial to help move the data from `flowData` into your dictionary.


```python
# do not edit flowData: this is dummy flow data
flowData = [
  ["sampleID", "CD3", "CD4", "CD8"],
  ["stim", 58.3, 24.3, 20.5],
  ["noStim", 32.1, 34.2, 50.3],
  ["PMAstim", 34.3, 15.3, 31.3]
]

# type your code below:

```
<details>
  <summary>Question 3 answer</summary>
  
  ```python
  # do not edit flowData: this is dummy flow data
  flowData = [
    ["sampleID", "CD3", "CD4", "CD8"],
    ["stim", 58.3, 24.3, 20.5],
    ["noStim", 32.1, 34.2, 50.3],
    ["PMAstim", 34.3, 15.3, 31.3]
  ]

  # type your code below:
  flowDataDict = {}
  for i in range(0, len(flowData[0])):
    colName = flowData[0][i]
    
    values = []
    for j in range(1, len(flowData)):
      values.append(flowData[j][i])
    
    flowDataDict[colName] = values
  ```
</details>