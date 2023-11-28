#practice question 1
myFavoriteNumbers = [24,3,9,2,4]
myFavoriteNumbers.append(8)

print(myFavoriteNumbers[2])

print(myFavoriteNumbers[:3])

print(myFavoriteNumbers[::-1])

total = 0
for i in myFavoriteNumbers:
    total += i 
print(total)

#practice question 2
myFavoritePipettes = {
    "20ulPipette" : "shares tips with 200 uL pipettes...yay!",
    "1000ulPipette": "largeeee-ish volumes"
}

myFavoritePipettes["200uL"] = "much versatile, such wow"


#practice question 3
# do not edit flowData: this is dummy flow data
flowData = [
  ["sampleID", "CD3", "CD4", "CD8"],
  ["stim", 58.3, 24.3, 20.5],
  ["noStim", 32.1, 34.2, 50.3],
  ["PMAstim", 34.3, 15.3, 31.3]
]

# type your code below:
flowDataDict = {}

headers = flowData[0]
for columnName in headers:
    flowDataDict[columnName] = []

rows = []
for row in flowData[1:]:
    for j in range (len(headers)):
        flowDataDict[headers[j]].append(row[j])



    