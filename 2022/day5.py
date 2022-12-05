'''
This task was basically the implementation of 9 stacks with different pop/append mechanisms
The code is a bit ugly and works only for up to 9 stacks
'''

data = []
stacksOne = []
stacksTwo = []

with open('data/day5') as file:
    stacksRead = []
    while True:
        tmp = file.readline()
        stacksRead.append(tmp.replace('\n', ''))
        if tmp[1] == '1':
            file.readline()
            break

    for line in file:
        data.append(line.split())

# Create the n stacks and populate them
amountOfStacks = int(stacksRead[-1][-2])
lengthOfLine = len(stacksRead[-1])

for _ in range(1, lengthOfLine, 4):
    stacksOne.append([])
    stacksTwo.append([])

stacksRead.pop()

for i in range(len(stacksRead)-1, -1, -1):
    stackIndex = 1
    for j in range(1, lengthOfLine, 4):
        if stacksRead[i][j] != ' ':
            stacksOne[j - stackIndex].append(stacksRead[i][j])
            stacksTwo[j - stackIndex].append(stacksRead[i][j])
        stackIndex += 3


for command in data:
    moveAmount = int(command[1])
    fromStack = int(command[3]) - 1
    toStack = int(command[5]) - 1

    # Part 1
    for _ in range(moveAmount):
        element = stacksOne[fromStack].pop()
        stacksOne[toStack].append(element)

    # Part 2
    holder = stacksTwo[fromStack][-moveAmount:]
    stacksTwo[fromStack] = stacksTwo[fromStack][:-moveAmount]
    for i in holder:
        stacksTwo[toStack].append(i)


print("Task 1:", end="\t")
for i in stacksOne:
    print(i[-1], end="")
print("\nTask 2:", end="\t")
for i in stacksTwo:
    print(i[-1], end="")
