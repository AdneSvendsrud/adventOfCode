'''
The task was to check each pair of elves' cleaning areas (represented as numbers) for overlaps
Task 1 was to check if one of the elves fully contained the other
Task 2 was to check if there was any overlap at all
'''
data = []
overlappingPairsOne = 0
overlappingPairsTwo = 0

with open('data/day4') as file:
    for line in file:
        data.append(line.replace('\n', '').split(','))

for pair in data:
    firstRange = pair[0].split('-')
    secondRange = pair[1].split('-')
    elf1Start, elf1End = int(firstRange[0]), int(firstRange[1])
    elf2Start, elf2End = int(secondRange[0]), int(secondRange[1])

    # Part 1
    # check if the first elf's interval is strictly inside the second elf's interval and vice versa
    if (elf1Start >= elf2Start and elf1End <= elf2End) or (elf2Start >= elf1Start and elf2End <= elf1End):
        overlappingPairsOne += 1

    # Part 2
    # check if each elf's range is within the other's
    if (elf2Start <= elf1End <= elf2End) or (elf2Start <= elf1Start <= elf2End) \
        or \
        (elf1Start <= elf2Start <= elf1End) or (elf1Start <= elf2End <= elf1End):
        overlappingPairsTwo += 1

print(f"Task 1: {overlappingPairsOne}")
print(f"Task 2: {overlappingPairsTwo}")
