
data = []
itemsFound = {}
sumPartOne = 0


groupItems = {}
sumPartTwo = 0

# the priorities of each item is their index + 1
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# initialize the dictionary
for char in chars:
    itemsFound[char] = 0
    groupItems[char] = 0

with open('data/day3') as file:
    for line in file:
        data.append(line.replace('\n', ''))


# Part 1
for idx, i in enumerate(data):
    splitAt = len(i) // 2
    firstHalf = i[:splitAt]
    secondHalf = i[splitAt:]

    for item in secondHalf:
        if item in firstHalf:
            itemsFound[item] += 1
            break

for key, value in itemsFound.items():
    for _ in range(value):
        sumPartOne += chars.index(key) + 1

# Part 2
for i in range(0, len(data), 3):
    amountItems = {}
    for j in data[i]:
        if j not in amountItems.keys():
            amountItems[j] = 1

    for j in data[i+1]:
        # if the item is not shared amountitems[j] raises a KeyError
        if j in amountItems.keys():
            if amountItems[j] < 2:
                amountItems[j] += 1

    for j in data[i+2]:
        if j in amountItems.keys():
            if amountItems[j] == 2:
                groupItems[j] += 1
                break

for key, value in groupItems.items():
    for _ in range(value):
        sumPartTwo += chars.index(key) + 1

# Output
print(f"Task 1: {sumPartOne}")
print(f"Task 2: {sumPartTwo}")
