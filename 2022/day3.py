'''
Part 1 of the task was to find the item stored in each of the two halves (compartments) of all elf's rucksacks
Part 2 of the task was to find out the authenticity badge for each group of elves (size 3), which was their shared item
'''
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
for rucksack in data:
    splitAt = len(rucksack) // 2
    firstHalf = rucksack[:splitAt]
    secondHalf = rucksack[splitAt:]

    for item in secondHalf:
        if item in firstHalf:
            itemsFound[item] += 1
            break

for key, value in itemsFound.items():
    for _ in range(value):
        sumPartOne += chars.index(key) + 1

# Part 2
for index in range(0, len(data), 3):
    for j in data[index]:
        if j in data[index+1] and j in data[index+2]:
            groupItems[j] += 1
            break

for key, value in groupItems.items():
    for _ in range(value):
        sumPartTwo += chars.index(key) + 1

# Output
print(f"Task 1: {sumPartOne}")
print(f"Task 2: {sumPartTwo}")
