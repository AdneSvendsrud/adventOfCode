'''
This task was to enumerate over a 2d array and figure out which values were "visible" from the outside, meaning
that value was higher than all else in their row/column in a direction.

I am not very happy with my solution, but it works
'''

data = []
visibility = []
maxScenicScore = -1

with open('data/day8') as file:
    for colIndex, line in enumerate(file):
        line = line.strip()
        data.append(line)

# top + bottom + left + right minus the corners
sumVisibleTrees = len(data[0]) * 2 + (len(data) - 2) * 2
for colIndex, column in enumerate(data):
    if colIndex == 0 or colIndex == len(data) - 1:
        continue
    for treeIndex, tree in enumerate(column):
        if treeIndex == 0 or treeIndex == len(data) - 1:
            continue

        # find all neighbors and check against them
        tree = int(tree)

        # Could probably be done using slicing directly instead of a list comprehension
        left = [int(trees) for trees in column[:treeIndex]]
        right = [int(trees) for trees in column[treeIndex + 1:]]
        up = [int(treeRow[treeIndex]) for treeRow in data[:colIndex]]
        down = [int(treeRow[treeIndex]) for treeRow in data[colIndex + 1:]]
        lowestTree = min(max(left), max(right), max(up), max(down))
        if tree > lowestTree:
            sumVisibleTrees += 1

        scenicScore = 0
        views = [0, 0, 0, 0]
        leftView, rightView, upView, downView = 0, 0, 0, 0

        # split into function
        up = up[::-1]
        left = left[::-1]
        for a in range(len(up)):
            upView += 1
            if tree <= up[a]:
                break

        for a in range(len(left)):
            leftView += 1
            if tree <= left[a]:
                break

        for a in range(len(right)):
            rightView += 1
            if tree <= right[a]:
                break

        for a in range(len(down)):
            downView += 1
            if tree <= down[a]:
                break

        scenicScore = leftView * rightView * upView * downView
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore

print("SOLUTION\n___________________________________________________")
print(f"Task 1: {sumVisibleTrees}")
print(f"Task 2: {maxScenicScore}")
