'''
The task was to follow the strategy guide, which led to 9 different outcomes due to the rules of rock paper scissors
I figured my code would be a lot easier to read if I used dictionaries to look up the outcome of the games instead
of having to "compute" it every time.
Task two is a bit less readable, but not so much that I would want to restructure or rename variables
A, X - rock
B, Y - paper
C, Z - scissors
'''

data = []
points = {'X': 1, 'Y': 2, 'Z': 3, 'win': 6, 'draw': 3, 'loss': 0}
totalScoreTaskOne = 0
totalScoreTaskTwo = 0

scenariosTaskOne = {
    'A': {'X': 'draw', 'Y': 'win', 'Z': 'loss'},
    'B': {'X': 'loss', 'Y': 'draw', 'Z': 'win'},
    'C': {'X': 'win', 'Y': 'loss', 'Z': 'draw'}
}

# This dictionary takes  the same input, but instead outputs either the gamestate or the expected move
scenariosTaskTwo = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'},
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}

with open('data/day2') as file:
    for line in file:
        data.append(line.split())

for i in data:
    # Task 1
    # win, loss, draw
    gamestateOne = scenariosTaskOne[i[0]][i[1]]
    totalScoreTaskOne += points[i[1]] + points[gamestateOne]

    # Task 2
    gamestateTwo = scenariosTaskTwo[i[1]]
    myMove = scenariosTaskTwo[i[0]][i[1]]
    totalScoreTaskTwo += points[myMove] + points[gamestateTwo]

print(f"Task 1:\t{totalScoreTaskOne} points")
print(f"Task 2:\t{totalScoreTaskTwo} points")
