# Dictionaries: another data structure in Python
For today's practice questions, you will need one of Python data structures which is called a **dict** (in R, there are multiple data structures that work similarly. One of these structures is called a named vector and the other is a list (yes, this is confusing nomenclature but for now let's just worry about the Python nomenclature and not R)). A `dict` is a dictionary, where we store key and value pairs. As the name implies, a real world dictionary works the same way. We provide the word "mountain" (i.e. the key) and we can access the definition (i.e. the value).

To instantiate (i.e create) a `dict`, we use curly brackets to denote a `dict`.

```python
myDict = {}
```

`myDict` is what we call an "empty dictionary" which means it has no elements in it. But let's go ahead and create a new `dict` that has something in it:

```python
anotherDict = {
  "mountain": "a large natural elevation of the earth's surface rising abruptly from the surrounding level; a large steep hill.",
  "hilarious": "extremely amusing"
}
```

`anotherDict` has 2 key-value pairs. One of the keys `mountain` *specifically* refers to the value `"a large natural elevation of the earth's surface rising abruptly from the surrounding level; a large steep hill."` (which is of type string). Note the usage of a colon to separate key and value. We also have a second key `hilarious` that refers to a different value. We separate key-value pairs by using a comma.

## What can be a key?
Keys must be unique in a dictionary, which makes sense since you wouldn't want one key to mean different things. Typically keys are strings or numbers. They cannot be lists or dictionaries.

## What can be a value?
Anything! This is what makes dictionaries very useful. For instance, I have changed the value of the `mountain` key to be a list of definitions.

```python
anotherDict = {
  "mountain": ["a large natural elevation of the earth's surface rising abruptly from the surrounding level; a large steep hill.",
    "a large pile or quantity of something."],
  "hilarious": "extremely amusing"
}
```

## How do I access data in a dictionary?
Please observe the below code:
```python
anotherDict["mountain"] # this will return ["a large natural elevation of the earth's surface rising abruptly from the surrounding level; a large steep hill.", "a large pile or quantity of something."]

anotherDict["mountain"][1] # this will return the 2nd element in the list, "a large pile or quantity of something." 

anotherDict["hilarious"] # this will return "extremely amusing"

anotherDict["fun"] # this will return a KeyError because the key "fun" doesn't exist in the dictionary
```

As you see from the last example, an error will occur when asking a dictionary to return the value of a key that doesn't exist. To solve this, we have to check first if the key is present to escape this error. Please observe below:

```python
if "fun" in anotherDict:
  print(anotherDict["fun"])

else:
  print("anotherDict doesn't have this key")
```

## Onto using a dictionary
Great! We now have a data structure, but how do I add or remove elements to it? Or change elements? Let's see how we can do that.

We can add elements as shown in the below chunk. I'm adding a new key-value pair in the last line of the chunk.

```python
peopleInTheLab = {
  "betina": "loves popping bubble wrap",
  "greg": "baloo's dad",
  "jake": "a prolific baker"
}

peopleInTheLab["kya"] = "a fantastic roller skater"
```

We can also remove elements from a dictionary by using `del` or `.pop()`.
```python
myTemporaryDict = {
  3: "hello",
  4: "hi",
  5: "hola"
}

del myTemporaryDict[3] # this will remove the key-value pair belonging to the key 3
myTemporaryDict.pop(4, None) # this will return the value belonging to the key 4 and remove that key-value pair

myTemporaryDict.pop(15, "uh oh") # this will return "uh oh" since the key 15 doesn't exist. If we replace "uh oh" with None, the function will return the value None if the key doesn't exist
```

We can change the values by using the index operator to reference specific keys as shown below:
```python
myTemporaryDict = {
  3: "hello",
  4: "hi",
  5: "hola"
}

myTemporaryDict[3] = "hello hello hello!"
```

## Using loops to work with dicts
We can use a `for` loop to iterate through the keys of a dictionary. IMPORTANT: you can NOT assume that the order of keys is the same order as what you initially set the dictionary as. This is because Python will automatically arrange the order of keys to allow for efficiency in memory storage and access.

```python
myTemporaryDict = {
  3: "yes",
  "hello": "maybe",
  5: "no"
}

for k in myTemporaryDict:
  print(myTemporaryDict[k])

# this will print out the following
# NOTE THAT AGAIN, one can NOT assume the order of keys is the same as our initial declaration

# "yes"
# "no"
# "maybe"
```