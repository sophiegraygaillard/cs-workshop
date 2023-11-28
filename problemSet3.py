#problem 1
mySum = 0 
for i in range(0,1000,1):
    if i % 3 == 0 or i % 5 == 0:
        mySum += i 

print(mySum)


#problem 6 
mySum = 0 
otherSum = 0
for i in range(1,101,1):
    mySum += i**2
    otherSum += i 
print(otherSum**2 - mySum)


#problem 2 
previous = 0
mySum = 0
otherSum = 0
i = 1
while i < 4e6: 
    mySum = i + previous
    previous = i
    i = mySum
    if mySum % 2 == 0:
        otherSum += mySum
print(otherSum)   


#problem 25
previous = 0
mySum = 0
otherSum = 0
i = 1
step = 1
while i > 0: 
    mySum = i + previous
    previous = i
    i = mySum
    step += 1
    count = 0
    n = mySum
    while(n>0):
        count = count + 1
        n=n//10  
    if count == 1000:
        break   
print(step)  


#problem 5 
i=19
while True:
    divisible = True
    for n in range (19,1,-1):
        if i % n != 0:
            divisible = False
            break
    
    if divisible:
        break
    
    i+=19
print(i)




