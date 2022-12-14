'''
This task needed management of worry levels in part 2, which was the biggest problem here.
'''

class Monkey:
    def __init__(self, monkey_items, monkey_operation, test_divisible_by, test_true, test_false):
        self.items = monkey_items
        self.operation = lambda old: eval(monkey_operation)
        self.test = lambda worry: test_true if worry % test_divisible_by == 0 else test_false
        self.inspected = 0

    def turn_part1(self):
        for idx, i in enumerate(self.items):
            self.inspected += 1
            self.items[idx] = self.operation(i) // 3
            i = self.items[idx]
            monkeysOne[self.test(i)].items.append(i)
        self.items = []

    def turn_part2(self, lcm):
        for idx, i in enumerate(self.items):
            self.inspected += 1
            self.items[idx] = self.operation(i) % lcm
            i = self.items[idx]
            monkeysTwo[self.test(i)].items.append(i)
        self.items = []


monkeysOne = []
monkeysTwo = []
lcm = 1  # All monkeys have a prime number, so their lcm is just each number multiplied by each other
# used to manage worry-levels in part 2
with open('data/day11') as file:
    while True:
        monkeyInfo = []
        for _ in range(6):
            monkeyInfo.append(file.readline().strip().split(':'))

        if monkeyInfo[-1][0] == '':
            break
        items = []
        for item in monkeyInfo[1][1].replace(' ', '').split(','):
            items.append(int(item))

        operation = monkeyInfo[2][1].replace(' ', '')[4:]
        divisible_by = int(monkeyInfo[3][1].replace(' ', '').split('by')[1])
        throw_true = int(monkeyInfo[4][1].replace(' ', '').split('monkey')[1])
        throw_false = int(monkeyInfo[5][1].replace(' ', '').split('monkey')[1])
        lcm *= divisible_by
        monkeysOne.append(Monkey(items[:], operation, divisible_by, throw_true, throw_false))
        monkeysTwo.append(Monkey(items[:], operation, divisible_by, throw_true, throw_false))
        file.readline()  # read the empty line after each monkey's definition

# part 1
for _ in range(20):
    for idx, monkey in enumerate(monkeysOne):
        monkey.turn_part1()

# max monkey business
monkeyBusiness = [-1, -1]
for monkey in monkeysOne:
    if monkey.inspected > monkeyBusiness[0]:
        monkeyBusiness[1] = monkeyBusiness[0]
        monkeyBusiness[0] = monkey.inspected
        continue

    if monkey.inspected > monkeyBusiness[1]:
        monkeyBusiness[1] = monkey.inspected

print(f"Part 1: {monkeyBusiness[0] * monkeyBusiness[1]}")

# Part 2
for _ in range(10000):
    for idx, monkey in enumerate(monkeysTwo):
        monkey.turn_part2(lcm)


monkeyBusiness = [-1, -1]

for monkey in monkeysTwo:
    if monkey.inspected > monkeyBusiness[0]:
        monkeyBusiness[1] = monkeyBusiness[0]
        monkeyBusiness[0] = monkey.inspected
        continue

    if monkey.inspected > monkeyBusiness[1]:
        monkeyBusiness[1] = monkey.inspected

print(f"Part 2: {monkeyBusiness[0] * monkeyBusiness[1]}")
