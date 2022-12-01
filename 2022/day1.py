'''
The task was to find the highest amount of calories and sum the top three elves' inventories together.
CaloryArray contains all the elves' inventories, which we can sort and sum to suit our needs.
Task 1 is solved by simply finding the largest value, max(caloryArray)
Task 2 is solved by summing the top three largest values, found by sorting, slicing and summing caloryArray
'''
caloryArray = []

with open('data/day1') as file:
    tmpCalories = 0
    for line in file:
        tmpStr = line.replace('\n', '')
        if tmpStr != '':
            tmpCalories += int(tmpStr)
        else:
            caloryArray.append(tmpCalories)
            tmpCalories = 0

    if tmpCalories:
        caloryArray.append(tmpCalories)

print(f"Task 1:\t{max(caloryArray)} kcal")
print(f"Task 2:\t{sum(sorted(caloryArray)[-3:])} kcal")
